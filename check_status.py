import requests
import os

update_url = os.environ['UPDATE_URL']
auth_token = os.environ['AUTH_TOKEN']
build_id = os.environ['BUILD_ID']
pod_url = os.environ['POD_URL']

# params = {"id": str(db_id), "url": str(pod_url)+":8069"}
params = {"id": str(build_id)}
headers = {"Authorization": f"Bearer {auth_token}"}

response = requests.get(update_url, params=params, headers=headers)
if response.status_code == 200:
    print("Request was successful")
    print("Response content:", response.text)
else:
    print("Request failed with status code:", response.status_code)
    print("Response content:", response.text)


# response_app = requests.get(str(pod_url)+":8069")
# if response_app.status_code == 200:
#     print("Request on app was successful")
#     print("Your app is running....")
# else:
#     print("Request failed with status code:", response_app.status_code)
#     print("Response content:", response_app.text)
