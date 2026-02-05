import streamlit as st
from resume_generator import generate_resume
from cover_letter_generator import generate_cover_letter
from pdf_export import export_to_pdf

st.set_page_config(
    page_title="AI Resume & Cover Letter Generator",
    page_icon="📄",
    layout="wide",
)

st.title("AI Resume & Cover Letter Generator")
st.markdown("Generate professional resumes and cover letters powered by OpenAI GPT-4o.")

# --- Sidebar: API Key & Mode ---
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("OpenAI API Key", type="password")
    mode = st.radio("What do you want to generate?", ["Resume", "Cover Letter"])
    st.markdown("---")
    st.markdown("Built by **Ajaykumar**")

if not api_key:
    st.info("Enter your OpenAI API key in the sidebar to get started.")
    st.stop()

# --- Common Inputs ---
st.header("Your Details")

col1, col2 = st.columns(2)
with col1:
    full_name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    location = st.text_input("Location (City, Country)")

with col2:
    linkedin = st.text_input("LinkedIn URL (optional)")
    github = st.text_input("GitHub URL (optional)")
    portfolio = st.text_input("Portfolio URL (optional)")

st.markdown("---")

skills = st.text_area("Skills (comma-separated)", placeholder="Python, Machine Learning, React, SQL, ...")
experience = st.text_area(
    "Work Experience",
    placeholder="Describe your work experience. Include company names, roles, duration, and key achievements.",
    height=150,
)
education = st.text_area(
    "Education",
    placeholder="Degree, University, Year of graduation, relevant coursework...",
    height=100,
)
projects = st.text_area(
    "Projects (optional)",
    placeholder="Describe notable projects with technologies used and outcomes.",
    height=100,
)

# --- Mode-specific inputs ---
if mode == "Cover Letter":
    st.markdown("---")
    st.header("Job Details")
    company_name = st.text_input("Company Name")
    job_title = st.text_input("Job Title")
    job_description = st.text_area(
        "Job Description",
        placeholder="Paste the job description here...",
        height=150,
    )

st.markdown("---")
tone = st.selectbox("Tone", ["Professional", "Friendly", "Confident", "Formal"])

# --- Generate ---
if st.button("Generate", type="primary", use_container_width=True):
    if not full_name:
        st.error("Please enter your full name.")
        st.stop()

    user_info = {
        "full_name": full_name,
        "email": email,
        "phone": phone,
        "location": location,
        "linkedin": linkedin,
        "github": github,
        "portfolio": portfolio,
        "skills": skills,
        "experience": experience,
        "education": education,
        "projects": projects,
        "tone": tone,
    }

    with st.spinner("Generating with AI..."):
        if mode == "Resume":
            result = generate_resume(api_key, user_info)
        else:
            if not company_name or not job_title:
                st.error("Please enter the company name and job title.")
                st.stop()
            job_info = {
                "company_name": company_name,
                "job_title": job_title,
                "job_description": job_description,
            }
            result = generate_cover_letter(api_key, user_info, job_info)

    if result:
        st.markdown("---")
        st.header(f"Your {mode}")
        st.markdown(result)

        # Export options
        col_a, col_b = st.columns(2)
        with col_a:
            st.download_button(
                label="Download as Text",
                data=result,
                file_name=f"{mode.lower().replace(' ', '_')}_{full_name.replace(' ', '_')}.txt",
                mime="text/plain",
            )
        with col_b:
            pdf_bytes = export_to_pdf(result, full_name, mode)
            st.download_button(
                label="Download as PDF",
                data=pdf_bytes,
                file_name=f"{mode.lower().replace(' ', '_')}_{full_name.replace(' ', '_')}.pdf",
                mime="application/pdf",
            )
