#!/bin/bash

# Check if the repository already exists
repo_info=$(aws ecr describe-repositories --repository-names $ECR_REPO_NAME --region eu-west-2 2>/dev/null)

# If the repository does not exist, create it
if [ -z "$repo_info" ]; then
    echo "Repository does not exist. Creating..."
    create_response=$(aws ecr create-repository --repository-name $ECR_REPO_NAME --region eu-west-2)
    repository_uri=$(echo $create_response | jq -r '.repository.repositoryUri')
    echo "Repository created with URI: $repository_uri"
else
    repository_uri=$(echo $repo_info | jq -r '.repositories[0].repositoryUri')
    echo "Repository already exists with URI: $repository_uri"
fi

export repository_uri=$repository_uri
