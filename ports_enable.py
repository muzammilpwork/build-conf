import os
import subprocess

get_scgrp_cmd = "aws ec2 describe-instances --filters 'Name=tag-key,Values=kubernetes.io/cluster/my-cluster' --query 'Reservations[*].Instances[*].SecurityGroups[*].GroupId' --output text"
result = subprocess.run(get_scgrp_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
if result.returncode == 0:
    print("Command output:", result.stdout)
else:
    print("Command failed. Error message:", result.stderr)
sce_grp = result.stdout
os.environ["SCE_GRP"] = str(sce_grp).strip()
