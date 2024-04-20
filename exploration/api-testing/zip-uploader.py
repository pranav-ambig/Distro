# write a code to upload a zip file to a localhost server

import requests

LOC = 'phase3/godknows.zip'

url = 'http://localhost:5000/upload-zip'
files = {'file': open(LOC, 'rb')}
response = requests.post(url, files=files)
print(response.text)
