!pip install groq pdfplumber reportlab python-dotenv
from groq import Groq

GROQ_API_KEY = "YOUR_GROQ_API_KEY"

client = Groq(api_key=GROQ_API_KEY)
from google.colab import files

uploaded = files.upload()

pdf_file = list(uploaded.keys())[0]

print("Uploaded:", pdf_file)
import pdfplumber

def extract_pdf_text(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text

syllabus_text = extract_pdf_text(pdf_file)

print("Characters Extracted:", len(syllabus_text))
prompt = f"""
You are an expert university question paper setter.

Generate a Semester End Examination Question Paper.

STRICTLY FOLLOW THIS FORMAT.

------------------------------------------------------------
Sri Eshwar college of engineering
Autonomous Semester End Examination

Degree & Branch:
Subject Code:
Subject Name:
Regulation:

Duration: 3 Hours                    Maximum Marks: 100

Answer ALL Questions

PART A – (10 × 2 = 20 Marks)

1.
2.
3.
4.
5.
6.
7.
8.
9.
10.

PART B – (5 × 16 = 80 Marks)

11. a)
(i)
(ii)

OR

b)

12. a)
(i)
(ii)

OR

b)
(i)
(ii)

13. a)
(i)
(ii)

OR

b)

14. a)

OR

b)
(i)
(ii)

15. a)

OR

b)

Total Marks = 100

Rules:
1. Questions only from syllabus.
2. Cover all units.
3. University-level questions.
4. Return only the question paper.

SYLLABUS:

{syllabus_text}
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.7,
    max_tokens=4000
)

question_paper = response.choices[0].message.content

print(question_paper)
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet

pdf_name = "generated_question_paper.pdf"

doc = SimpleDocTemplate(pdf_name)

styles = getSampleStyleSheet()

elements = []

for line in question_paper.split("\n"):

    elements.append(
        Paragraph(
            line.replace(" ", "&nbsp;"),
            styles["Normal"]
        )
    )

    elements.append(Spacer(1, 3))

doc.build(elements)

print("PDF Created:", pdf_name)
from google.colab import files

files.download("generated_question_paper.pdf")
