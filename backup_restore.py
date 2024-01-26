import requests
import os


existing_build_url = os.environ['EXISTING_BUILD_URL']
new_build_url = os.environ['SUB_DOMAIN']

url = f"https://nomanjallal-addons-new-test-app6yodttirbe3.erp-deploy.com/web/database/backup"
data = {
    "master_pwd": 'abctest123',
    "name": 'postgres',
    "backup_format": "zip"
}
response = requests.post(url, data=data)
with open('backup.zip', 'wb') as writer:
    writer.write(response.content)


with open('backup.zip', 'rb') as reader:
    file_content = reader.read()
restore_payload = {
    'name': 'postgres',
    'master_pwd': 'abctest123',
}

url = f'https://nomanjallal-addons-new-test-app7iz6ocf5gze.erp-deploy.com/web/database/restore'
files = {'backup_file': file_content}

restore_response = requests.post(url, data=restore_payload, files=files)
