# write a code to upload a zip file to a localhost server

import requests

url = 'http://localhost:5000/upload-zip'
files = {'file': open('temp5.zip', 'rb')}
response = requests.post(url, files=files)
print(response.text)
