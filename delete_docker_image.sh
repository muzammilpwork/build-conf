#!/bin/bash

# Obtain the access token
HUB_TOKEN=$(curl -s -H "Content-Type: application/json" -X POST -d "{\"username\": \"$DOCKER_USERNAME\", \"password\": \"$DOCKER_PASSWORD\"}" https://hub.docker.com/v2/users/login/ | jq -r .token)

curl -i -X DELETE   -H "Accept: application/json"   -H "Authorization: JWT $HUB_TOKEN"   https://hub.docker.com/v2/repositories/$DOCKER_USERNAME/$HUB_REPO/tags/$HUB_TAG/
