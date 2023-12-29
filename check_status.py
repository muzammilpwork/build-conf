import requests

update_url = os.environ['UPDATE_URL']
auth_token = os.environ['AUTH_TOKEN']
db_id = os.environ['APP_POD_DB_ID']
pod_url = os.environ['POD_URL']

params = {"id": str(db_id), "url": str(pod_url)}
headers = {"Authorization": f"Bearer {auth_token}"}

response = requests.get(update_url, params=params, headers=headers)

# Check the response
if response.status_code == 200:
    print("Request was successful")
    print("Response content:", response.text)
else:
    print("Request failed with status code:", response.status_code)
    print("Response content:", response.text)
