# AI-Powered Resume Analyzer

## Overview

A simple web application that allows users to upload their resume and paste a job description to assess how well their skills align. The app uses Natural Language Processing (NLP) to extract skills and calculate a match percentage.

## Features

- Upload resume in PDF format
- Paste job description text
- Extract skills using spaCy NLP
- Compare resume skills to job requirements
- Display a match score and list of matched/missing skills

## Technologies Used

- Python
- Streamlit (web application framework)
- spaCy (natural language processing)
- PyMuPDF (PDF parsing)

## Project Structure

```
resume_analyzer/
├── app.py                # Main Streamlit application
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Getting Started

### Clone the Repository

```
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
```

### Install Dependencies

```
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### Run the Application

```
streamlit run app.py
```

The app will be available at:

```
http://localhost:8501
```

## Deploying on Streamlit Cloud

1. Push your code to a public GitHub repository
2. Go to https\://streamlit.io/cloud and sign in with GitHub
3. Click "New app"
4. Select your repository and set `app.py` as the entry point
5. Click "Deploy"

## Usage Example

1. Upload a resume (PDF format)
2. Paste a job description into the text area
3. Click "Analyze"

The application will display:

- Resume Match Score (e.g., 66.67%)
- List of Matched Skills
- List of Missing Skills

## Sample Output

```
Resume Match Score: 66.67%
Matched Skills: {'Python', 'SQL', 'Flask', 'Git'}
Missing Skills: {'Django', 'Docker'}
```

## requirements.txt

```
streamlit
spacy
PyMuPDF
```

## Learning Outcomes

- Implemented a skill-matching algorithm using Python sets
- Built a user-friendly web interface using Streamlit
- Used spaCy to extract relevant information from text
- Parsed PDF files using PyMuPDF
- Deployed a functional app on Streamlit Cloud

## Resume Bullet Point

```
- Developed a web-based Resume Analyzer using Python, Streamlit, spaCy, and PyMuPDF to extract and compare skills from resumes and job descriptions
- Designed an intuitive interface and implemented a skill-matching algorithm to display a compatibility score
- Deployed the application on Streamlit Cloud for public access and demonstration
```

---

This project can be used in technical interviews, portfolios, or shared with recruiters to demonstrate your skills in natural language processing, web development, and deployment.

