from pypdf import PdfReader
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()


def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text



client = Groq(api_key=os.getenv("GROQ_API_KEY"))



def analyze_resume(resume_text, job_desc):
    prompt = f"""
    You are an AI Resume Analyzer.

    Compare the resume and job description.

    Resume:
    {resume_text}

    Job Description:
    {job_desc}

    Provide:
    1. Skill Match Percentage
    2. Missing Skills
    3. Improvement Suggestions
    4. ATS Optimization Tips
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
    )

    return response.choices[0].message.content