import subprocess

class RDPEnabler:
    def __init__(self):
        self.reg_command = 'reg add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f'
        self.firewall_command = 'netsh advfirewall firewall add rule name="Remote Desktop" dir=in action=allow protocol=TCP localport=3389'

    def enable_rdp(self):
        try:
            subprocess.check_call(self.reg_command, shell=True)
            subprocess.check_call(self.firewall_command, shell=True)
            print('RDP enabled successfully.')
        except subprocess.CalledProcessError as e:
            print('Error enabling RDP:', e)
