# AI Question Paper Generator using Groq

## Overview

AI Question Paper Generator is an intelligent system that automatically generates university-style semester examination question papers from a syllabus PDF. The application extracts syllabus content, analyzes the topics, and uses Groq's LLM to generate a complete question paper following the Sri Eshwar College of Engineering examination pattern.

The generated question paper is automatically exported as a PDF and made available for download.

---

## Features

* Upload syllabus PDF directly in Google Colab
* Automatic syllabus text extraction
* AI-powered question generation using Groq LLM
* Generates questions only from the uploaded syllabus
* Covers all units and topics
* Follows university examination format
* Exports question paper as PDF
* One-click download of generated question paper

---

## Technology Stack

* Python
* Groq API
* Llama 3.3 70B Versatile
* PDFPlumber
* ReportLab
* Google Colab

---

## Workflow

1. Upload syllabus PDF.
2. Extract text from the PDF.
3. Send syllabus content to the Groq LLM.
4. Generate a complete semester-end question paper.
5. Convert generated content into PDF format.
6. Download the generated question paper.

---

## Question Paper Format

The generated question paper follows the Sri Eshwar College of Engineering pattern:

### Part A

* 10 Questions
* 2 Marks each
* Total: 20 Marks

### Part B

* 5 Questions
* Internal Choice (OR Pattern)
* 16 Marks each
* Total: 80 Marks

### Total Marks

100 Marks

---

## Project Structure

```text
AI-Question-Paper-Generator/
│
├── AI_Question_Paper_Generator.ipynb
├── README.md
├── generated_question_paper.pdf
└── sample_syllabus.pdf
```

---

## Installation

Install required libraries:

```bash
pip install groq
pip install pdfplumber
pip install reportlab
pip install python-dotenv
```

---

## Usage

### Step 1

Open the notebook in Google Colab.

### Step 2

Enter your Groq API key.

### Step 3

Upload the syllabus PDF.

### Step 4

Run all notebook cells.

### Step 5

Download the generated question paper PDF.

---

## Sample Input

* Subject Syllabus PDF
* University Curriculum PDF

---

## Sample Output

* AI-generated Semester End Examination Question Paper
* PDF format output

---

## Future Enhancements

* Support multiple university formats
* Question difficulty customization
* Bloom's Taxonomy-based question generation
* Unit-wise question distribution control
* Faculty review and editing interface
* RAG-based generation using previous year question papers
* Web application deployment

---

## Applications

* Colleges and Universities
* Faculty Members
* Examination Cell Automation
* Academic Content Generation
* Educational Institutions

---

