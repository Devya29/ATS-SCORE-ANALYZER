import re
import pdfplumber

# -------------------- CONFIG --------------------

STOPWORDS = {
    "and", "or", "the", "is", "are", "a", "an", "to", "for",
    "with", "of", "in", "on", "we", "i", "you", "it", "this",
    "that", "as", "by", "from", "at","good","have","reponsibility"
}

SKILLS = {
    "python", "c++", "java", "sql", "git",
    "data", "structures", "algorithms",
    "ai", "machine", "learning", "ml",
    "problem", "problemsolving", "mongo","web development", "html", "css", "javascript", "frontend", "responsive design"
}

WEIGHTS = {
    "python": 3,
    "data": 2,
    "structures": 2,
    "algorithms": 2,
    "ai": 2,
    "problemsolving": 2,
    "git": 1,
    "sql": 2,
    "mongo": 1
}

SKILL_MAP = {
    "mysql": "sql",
    "postgresql": "sql",
    "mongodb": "mongo",
    "mongoose": "mongo",
    "problem": "problemsolving",
    "solving": "problemsolving",
    "webdev": "webdevelopment",
    "web-dev": "web development",
    "js":"javascript",
    "front-end":"frontend"
}

# -------------------- PDF UTILS --------------------

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

# -------------------- NLP HELPERS --------------------

def split_compound_by_skills(word):
    found = []
    for skill in SKILLS:
        if skill in word and skill not in found:
            found.append(skill)
    return found


def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z]', ' ', text)

    words = []

    for word in text.split():
        if word in STOPWORDS:
            continue

        split_skills = split_compound_by_skills(word)
        if len(split_skills) > 1:
            words.extend(split_skills)
            continue

        words.append(SKILL_MAP.get(word, word))

    return words


def word_frequency(words):
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq

# -------------------- CORE ANALYSIS --------------------

def analyze(resume_text, jd_text):
    resume_words = preprocess(resume_text)
    jd_words = preprocess(jd_text)

    resume_freq = word_frequency(resume_words)
    jd_freq = word_frequency(jd_words)

    matched = []
    missing = []

    for word in jd_freq:
        if word in SKILLS:
            if word in resume_freq:
                matched.append(word)
            else:
                missing.append(word)

    total_weight = sum(WEIGHTS.get(s, 1) for s in matched + missing)
    matched_weight = sum(WEIGHTS.get(s, 1) for s in matched)

    score = int((matched_weight / total_weight) * 100) if total_weight else 0

    return {
        "score": score,
        "matched": sorted(set(matched)),
        "missing": sorted(set(missing))
    }
