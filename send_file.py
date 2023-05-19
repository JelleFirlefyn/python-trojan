import ftplib
from pathlib import Path
from dotenv import load_dotenv
import os
from github import Github

load_dotenv()

FTP_HOST = os.getenv("ftp-host")
FTP_PORT = int(os.getenv("ftp-port"))
FTP_USER = os.getenv("ftp-user")
FTP_PASSWORD = os.getenv("ftp-password")

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