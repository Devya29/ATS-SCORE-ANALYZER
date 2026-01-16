# ATS Resume Score Analyzer

An Applicant Tracking System (ATS) inspired resume analyzer built using Python.  
This project analyzes how well a resume matches a given job description by extracting skills, handling noisy PDF text, and calculating a weighted ATS score.

---

## 📌 Overview

Modern ATS systems often reject resumes due to formatting issues, missing keywords, or poorly optimized content.  
This project simulates core ATS behavior by:

- Parsing resume PDFs
- Cleaning noisy and merged text
- Normalizing technical skills
- Matching resume skills against job requirements
- Generating an ATS compatibility score

---

## ✨ Key Features

- PDF resume text extraction
- Robust preprocessing for noisy PDF text
- Dynamic compound word handling (e.g. `DataStructuresAndAlgorithms`)
- Skill normalization (MySQL → SQL, MongoDB → Mongo)
- Weighted ATS score calculation
- Identification of missing skills
- Resume improvement suggestions
- Streamlit-ready web interface

---

## 🧱 Project Structure
```txt
ATS-SCORE-ANALYZER/
│
├── app.py                 # Streamlit frontend (UI)
├── ats_engine.py          # Core ATS logic
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── sample/
│   ├── resume_sample.pdf
│   └── job_description.txt
│
└── .gitignore
```



---

## ⚙️ How the System Works

1. Extracts raw text from resume PDF
2. Cleans and tokenizes noisy text
3. Dynamically splits merged skill words
4. Normalizes skill variations into canonical forms
5. Matches resume skills against job description
6. Computes a weighted ATS score
7. Generates resume improvement suggestions

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **pdfplumber**

---

## 📦 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/ATS-SCORE-ANALYZER.git
cd ATS-SCORE-ANALYZER
```

### 2️⃣ (Optional) Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project Locally
```bash
streamlit run app.py
```

Open the browser at:
```
http://localhost:8501
```

---

## 🧪 How to Use

1. Upload a resume PDF  
2. Paste the job description  
3. Click **Analyze**  
4. View:
   - ATS Score  
   - Matched Skills  
   - Missing Skills  
   - Resume Improvement Suggestions  

---

## 🌍 Deployment

The project is designed to be deployed on **Streamlit Cloud**.

### Deployment Steps:
1. Push the repository to GitHub  
2. Go to https://streamlit.io/cloud  
3. Connect your GitHub account  
4. Select this repository  
5. Choose `app.py` as the entry point  
6. Deploy 🚀  

---

## 👤 Author

**Devya Saigal**  
B.Tech Computer Science & Engineering  
Focused on DSA, AI, and backend systems  

- GitHub: https://github.com/Devya29  
- LeetCode: https://leetcode.com/u/Devya_Saigal-05/  

---

## 📄 License

This project is intended for educational and demonstration purposes.

