#!/bin/bash

git status

git add .

git commit -m "update on $(date) by $(whoami) on $(hostname)"

git push origin main
sleep 2s