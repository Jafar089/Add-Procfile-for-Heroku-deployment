import requests

url = 'http://127.0.0.1:5000/parse-resume'
file_path = 'Zain_Resume.pdf'

with open(file_path, 'rb') as f:
    files = {'file': f}
    response = requests.post(url, files=files)

print(response.json())
