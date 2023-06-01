#!/bin/bash

# branch=$(git symbolic-ref --short HEAD)
# modified_files=$(git status --porcelain | awk '{if ($1 == "M" || $1 == "A") print $2}')

# commit_message="Updated or added files on branch $branch:"
# for file in $modified_files; do
#   commit_message+=" $file"
# done



# git status

# git add .

# git commit -m "Update on by $(whoami) on $(hostname) for the files: $commit_message"

# # git push origin main



# sleep 2s





# Get the name of the current branch
branch=$(git symbolic-ref --short HEAD)

# Get the list of modified or added files
modified_files=$(git status --porcelain | awk '{if ($1 == "M" || $1 == "A") print $2}')

# Commit message mentioning the updated or added files and the branch
commit_message="Updated on branch $branch by $(whoami) on $(hostname) for the files: $modified_files"
for file in $modified_files; do
  commit_message+=" $file"
done

# Commit and push the changes
git add .
git commit -m "$commit_message"
git push origin $branch
