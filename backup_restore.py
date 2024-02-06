import requests
import os
import time 

existing_build_url = os.environ['EXISTING_BUILD_URL']
new_build_url = os.environ['SUB_DOMAIN']

url = f"{existing_build_url}/web/database/backup"
data = {
    "master_pwd": 'abctest123',
    "name": 'noman123',
    "backup_format": "zip"
}
response = requests.post(url, data=data)
with open('backup.zip', 'wb') as writer:
    writer.write(response.content)
print("Data has been backed up and response is: ", response.status_code)

with open('backup.zip', 'rb') as reader:
    file_content = reader.read()
restore_payload = {
    'name': 'noman123',
    'master_pwd': 'abctest123',
}

url = f'https://{new_build_url}.erp-deploy.com/web/database/restore'
files = {'backup_file': file_content}
count = 0
while True:
    restore_response = requests.post(url, data=restore_payload, files=files)
    if restore_response.status_code == 200 or count == 3:
        print("Data has been restored and response is: ", restore_response.content)
        break
    time.sleep(10)
