#!/bin/bash

message="first version, Lambda, S3 and API"
git status

git add .

git commit -m "update on $(date) by $(whoami) on $(hostname) for $message"

git push origin main
sleep 2s