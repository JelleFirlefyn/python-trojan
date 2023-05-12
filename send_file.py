import ftplib
from pathlib import Path

FTP_HOST = ""
FTP_PORT = 21
FTP_USER = ''
FTP_PASSWORD = ''

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