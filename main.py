from flask import Flask, request, jsonify
from parser import Parser
import os

app = Flask(__name__)

# Initialize parser object
parser = Parser()

@app.route('/')
def home():
    return "Flask is running!"

@app.route('/parse-resume', methods=['POST'])
def parse_resume():
    file = request.files.get('file')
    if not file:
        print("No file provided")
        return jsonify({"error": "No file provided"}), 400

    print(f"File received: {file.filename}")
    
    # Save the file to a temporary location
    file_path = os.path.join(os.getcwd(), file.filename)
    file.save(file_path)
    
    print(f"File saved to {file_path}")

    # Call the parser functions
    text = parser.extract_text_from_pdf(file_path)
    print("Text extracted from PDF")

    phone = parser.extract_contact_number(text)
    email = parser.extract_email(text)
    skills_list = ['Python', 'Data Analysis', 'C++', 'C', 'React', 'HTML5', 'CSS', 'Machine Learning', 'Communication', 'html', 'Deep Learning', 'SQL', 'Tableau']
    skills = parser.extract_skills(text, skills_list)
    education = parser.extract_education(text)

    print("Parsed data ready to be returned")

    # Return the parsed data
    return jsonify({
        'phone': phone,
        'email': email,
        'skills': skills,
        'education': education
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
