import requests
import os

update_url = os.environ['UPDATE_URL']
auth_token = os.environ['AUTH_TOKEN']
build_id = os.environ['BUILD_ID']


params = {"id": str(build_id), "type" : "delete"}
headers = {"Authorization": f"Bearer {auth_token}"}

response = requests.get(update_url, params=params, headers=headers)
if response.status_code == 200:
    print("Request was successful")
    print("Response content:", response.text)
else:
    print("Request failed with status code:", response.status_code)
    print("Response content:", response.text)
