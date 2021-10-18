import os
import subprocess

def get_submissions():
    return sorted([int(dir_name) for dir_name in os.listdir("submissions")])

for submission in get_submissions():
    submission_path = f"submissions/{submission}/cash.py"
    output_path = f"outputs/{submission}.txt"

    if not os.path.exists("outputs"):
        os.mkdir("outputs")

    with open(output_path, "w") as f:
        print(f"Testing - {submission_path} => {output_path}", end="", flush=True)
        
        exit_status = subprocess.call(["pytest", "--path", submission_path], stdout=f)

        print(f"{'  ' if submission < 10 else ''} | {'FAILED' if exit_status else 'SUCCESS'}")