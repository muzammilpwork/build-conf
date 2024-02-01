import requests
import os


existing_build_url = os.environ['EXISTING_BUILD_URL']
new_build_url = os.environ['SUB_DOMAIN']

url = f"https://{existing_build_url}/web/database/backup"
data = {
    "master_pwd": 'abctest123',
    "name": 'postgres',
    "backup_format": "zip"
}
response = requests.post(url, data=data)
with open('backup.zip', 'wb') as writer:
    writer.write(response.content)
print("Data has been backed up......")

with open('backup.zip', 'rb') as reader:
    file_content = reader.read()
restore_payload = {
    'name': 'postgres',
    'master_pwd': 'abctest123',
}

url = f'https://{new_build_url}.erp-deploy.com/web/database/restore'
files = {'backup_file': file_content}
restore_response = requests.post(url, data=restore_payload, files=files)
print("Data has been restored......")
