from openai import OpenAI


def generate_resume(api_key: str, user_info: dict) -> str:
    client = OpenAI(api_key=api_key)

    prompt = f"""Generate a professional resume in clean markdown format for the following person.
Use clear sections with headers. Make it ATS-friendly and well-structured.

Tone: {user_info['tone']}

Personal Information:
- Name: {user_info['full_name']}
- Email: {user_info['email']}
- Phone: {user_info['phone']}
- Location: {user_info['location']}
- LinkedIn: {user_info['linkedin']}
- GitHub: {user_info['github']}
- Portfolio: {user_info['portfolio']}

Skills: {user_info['skills']}

Work Experience:
{user_info['experience']}

Education:
{user_info['education']}

Projects:
{user_info['projects']}

Instructions:
- Use markdown formatting with clear section headers (##)
- Include a professional summary at the top
- Format work experience with bullet points highlighting achievements and impact
- Keep it concise, ideally fitting on 1-2 pages
- Use action verbs and quantify achievements where possible
- Make sure the skills section is well-organized
- Only include sections that have actual content provided
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are an expert resume writer. Generate clean, professional, ATS-friendly resumes in markdown format.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content
