#!/bin/bash


project="serverless-framework"



npm install --save serverless-webpack webpack serverless-s3-sync

# # create serverless instance
# serverless create \
#     --template aws-nodejs \
#     --path $project


# # deploy the project

# cd $project

serverless deploy

sleep 5s

