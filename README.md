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

