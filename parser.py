import re
from pdfminer.high_level import extract_text


class Parser:
    # extract text from pdf
    def extract_text_from_pdf(self, file_path):
        return extract_text(file_path)

    # contact number information from the text
    def extract_contact_number(self, resume_text):
        number = None
        pattern = r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
        match = re.search(pattern, resume_text)
        if match:
            number = match.group()
        return number

    # extract email information from the text
    def extract_email(self, resume_text):
        email = None
        all_words = resume_text.split()
        for i in all_words:
            if "@" in i:
                email = i.strip()
                break
        return email

    # skills information from the text
    def extract_skills(self, text, skills_list_to_compare):
        resume_skills = []
        for skill in skills_list_to_compare:
            pattern = r"\b{}\b".format(re.escape(skill))
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                resume_skills.append(skill)
        return resume_skills

    # extract education information from the text
    def extract_education(self, text):
        education = []
        education_keywords = ['Bsc', 'Bscs', 'B. Pharmacy', 'B Pharmacy', 'Msc', 'M. Pharmacy', 'Ph.D', 'Bachelor', 'Master']
        for keyword in education_keywords:
            pattern = r"(?i)\b{}\b".format(re.escape(keyword))
            match = re.search(pattern, text)
            if match:
                education.append(match.group())
        return education
