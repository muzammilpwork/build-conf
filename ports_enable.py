import os
import subprocess
import sys

port_list = sys.argv[1:]
get_scgrp_cmd = "aws ec2 describe-instances --filters 'Name=tag-key,Values=kubernetes.io/cluster/my-cluster' --query 'Reservations[*].Instances[*].SecurityGroups[*].GroupId' --output text"
result = subprocess.run(get_scgrp_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
if result.returncode == 0:
    print("Command output:", result.stdout)
else:
    print("Command failed. Error message:", result.stderr)
sce_grp = result.stdout
for port in port_list:
    # aws_command = ["aws", "ec2", "authorize-security-group-ingress", "--group-id", sce_grp, "--protocol", "tcp", "--port", port, "--cidr", "0.0.0.0/0"]
    # # cmd = f"aws ec2 authorize-security-group-ingress --group-id {sce_grp} --protocol tcp --port {port} --cidr 0.0.0.0/0"
    # print('####### ', aws_command)
    # # os.system(cmd)
    # subprocess.run(aws_command, check=True)
    
    aws_command = ["aws", "ec2", "authorize-security-group-ingress", "--group-id", sce_grp, "--protocol", "tcp", "--port", port, "--cidr", "0.0.0.0/0"]
    # Execute the command using subprocess and capture output
    result = subprocess.run(aws_command, capture_output=True, text=True)
    
    # Print stdout and stderr
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
    
    # Check if the command was successful
    if result.returncode == 0:
        print("Command executed successfully.")
    else:
        print("Command failed with return code:", result.returncode)
