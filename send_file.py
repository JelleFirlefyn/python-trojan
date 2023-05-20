import ftplib
from pathlib import Path
from dotenv import load_dotenv
import os
import subprocess

load_dotenv()

FTP_HOST = os.getenv("ftp-host")
FTP_PORT = int(os.getenv("ftp-port"))
FTP_USER = os.getenv("ftp-user")
FTP_PASSWORD = os.getenv("ftp-password")

# Comment this function when using the GitHub repository to store data:
def send_file(src_file):
    #Log file to an remote FTP server
    ftp = ftplib.FTP()
    ftp.connect(FTP_HOST, FTP_PORT)
    print (ftp.getwelcome())
    try:
        print ("Logging in...")
        ftp.login(FTP_USER, FTP_PASSWORD)
    except:
        "failed to login"

    file_path = Path(src_file)
    with open(file_path, 'rb') as file:
        ftp.storbinary(f'STOR {file_path.name}', file)


# Alternative way of saving host data using GitHub repository (read docs):
"""
REPO_URL = os.getenv("data_repo_url")
FOLDER_PATH = 'content'

#src_file var is an option to avoid changing all code to use this function:
def send_file(src_file, folder_path = FOLDER_PATH, repository_url = REPO_URL):
    # Initialize a new Git repository in the folder
    subprocess.run(['git', 'init'], cwd=folder_path)
    
    # Add all files in the folder to the repository
    subprocess.run(['git', 'add', '.'], cwd=folder_path)
    
    # Commit the changes
    subprocess.run(['git', 'commit', '-m', 'Initial commit'], cwd=folder_path)
    
    # Set the remote origin URL
    subprocess.run(['git', 'remote', 'add', 'origin', repository_url], cwd=folder_path)
    
    # Push the changes to the remote repository
    subprocess.run(['git', 'push', '-u', 'origin', 'master'], cwd=folder_path)
"""