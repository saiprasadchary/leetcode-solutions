import os
import subprocess

# Set the path to your LeetCode solutions folder
leetcode_solutions_path = "C:/Users/saipr/leetcode-solutions"
os.chdir(leetcode_solutions_path)

# Git commands to add, commit, and push new solutions
subprocess.run(["git", "add", "."])  # Add all new files to the staging area
subprocess.run(["git", "commit", "-m", "Add latest LeetCode solutions"])  # Commit the changes
subprocess.run(["git", "push", "origin", "main"])  # Push the changes to the GitHub repository
