# write a code to upload a zip file to a localhost server

import requests

url = 'http://localhost:5000/upload-zip'
files = {'file': open('example2.zip', 'rb')}
response = requests.post(url, files=files)
print(response.text)
