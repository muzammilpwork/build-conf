import subprocess
import time
import os

pod_name = os.environ['APP_POD_NAME']

command = 'kubectl get pod ' + str(pod_name) + ' -o jsonpath="{.status.phase}"'

count = 0
while count < 8:
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    pod_status = str(result.stdout).strip()
    if pod_status == "Running":
        break
    else:
      time.sleep(20)
      count += 1

if pod_status != "Running":
  raise Exception("Pod is not in running state")
