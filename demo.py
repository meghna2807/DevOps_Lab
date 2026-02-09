import os

os.system("git init")
os.system("git add .")
os.system('git commit -m "Initial commit"')
os.system("git branch -M main")
os.system("git remote add origin https://github.com/meghna2807/DevOps_Lab.git")
os.system("git push -u origin main")

print("Source code pushed to GitHub successfully")
