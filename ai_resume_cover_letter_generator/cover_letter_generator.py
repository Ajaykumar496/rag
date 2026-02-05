from openai import OpenAI


def generate_cover_letter(api_key: str, user_info: dict, job_info: dict) -> str:
    client = OpenAI(api_key=api_key)

    prompt = f"""Write a compelling cover letter in markdown format for the following candidate applying to a specific job.

Tone: {user_info['tone']}

Candidate Information:
- Name: {user_info['full_name']}
- Email: {user_info['email']}
- Phone: {user_info['phone']}
- Location: {user_info['location']}
- LinkedIn: {user_info['linkedin']}

Skills: {user_info['skills']}

Work Experience:
{user_info['experience']}

Education:
{user_info['education']}

Projects:
{user_info['projects']}

Job Details:
- Company: {job_info['company_name']}
- Position: {job_info['job_title']}
- Job Description:
{job_info['job_description']}

Instructions:
- Write a personalized cover letter that connects the candidate's experience to the job requirements
- Use markdown formatting
- Include a proper greeting and closing
- Highlight 2-3 key achievements or experiences that are most relevant to the role
- Show genuine interest in the company and role
- Keep it concise (3-4 paragraphs)
- End with a clear call to action
- Make it sound human and natural, not generic or templated
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are an expert cover letter writer. Write personalized, compelling cover letters that connect the candidate's experience to the specific job. Output in clean markdown.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content
