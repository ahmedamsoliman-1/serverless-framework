#!/bin/bash

modified_files=$(git status --porcelain | awk '{if ($1 == "M" || $1 == "A") print $2}')

commit_message=""
for file in $modified_files; do
  commit_message+=" $file"
done



git status

git add .

git commit -m "Update on by $(whoami) on $(hostname) for the files: $commit_message"

git push origin main



sleep 2s