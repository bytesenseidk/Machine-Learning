import os
import GPUtil
import psutil
import platform
import speedtest
from datetime import datetime


class SystemScanner(object):
    def get_size(self, bytes, suffix="B"):
        """
        Scale bytes to its proper format
        e.g:
            1253656 => '1.20MB'
            1253656678 => '1.17GB'
        """
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor


    def system_info(self):
        uname = platform.uname()
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        data = {
            "System":       uname.system, 
            "Node Name":    uname.node,   
            "Release":      uname.release,
            "Version":      uname.version,
            "architecture": uname.machine,
            "Processor":    uname.processor,
            "Boot Time": str(f"{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
        }
        return data


    def cpu_info(self):
        cpufreq = psutil.cpu_freq()
        data = {
            "Physical Cores": psutil.cpu_count(logical=False),
            "Total Cores": psutil.cpu_count(logical=True),
            "Max Frequency": str(f"{cpufreq.max:.2f}Mhz"),
            "Min Frequency": str(f"{cpufreq.min:.2f}Mhz"),
            "Current Frequency": str(f"{cpufreq.current:.2f}Mhz"),
            "Total Usage": str(f"{psutil.cpu_percent()}%")
        }
        return data
        

    def ram_info(self):
        svmem = psutil.virtual_memory()
        data = {
            "Total": self.get_size(svmem.total),
            "Available": self.get_size(svmem.available),
            "Used": self.get_size(svmem.used),
            "Percentage": str(f"{svmem.percent}%")
        }
        return data


    def gpu_info(self):
        gpus = GPUtil.getGPUs()
        data = {}
        for gpu in gpus:
            data["ID"] = gpu.id
            data["Name"] = gpu.name
            data["Load"] = f"{gpu.load*100}%"
            data["Free"] = f"{gpu.memoryFree} MB"
            data["Used"] = f"{gpu.memoryUsed} MB"
            data["Total"] = f"{gpu.memoryTotal} MB"
            data["Temp"] = f"{gpu.temperature} °C"
            data["UUID"] = gpu.uuid
        return data

    
    def disk_info(self):
        drive = psutil.disk_partitions()[0]
        disk_io = psutil.disk_io_counters()
        try:
            partition_usage = psutil.disk_usage(drive.mountpoint)
        except PermissionError:
            pass
        data = {
            "Device": drive.device,
            "Mountpoint": drive.mountpoint,
            "Filesystem": drive.fstype,
            "Total Size": self.get_size(partition_usage.total),
            "Used": self.get_size(partition_usage.used),
            "Free": self.get_size(partition_usage.free),
            "Percentage": str(f"{partition_usage.percent}%"),
            "Total Read": self.get_size(disk_io.read_bytes),
            "Total Write": self.get_size(disk_io.write_bytes)
        }
        return data
    
    def network_info(self):
        print("\nWill now do a scan, this won't take long...\n")
        scanner = psutil.net_if_addrs()
        interfaces = []
        for interface_name, _ in scanner.items():
            interfaces.append(str(interface_name))
        interface = interfaces[0]
        net_io = psutil.net_io_counters()
        speed = speedtest.Speedtest()
        data = {"Interface:" : interface,
                "Download:" : str(f"{round(speed.download() / 1_000_000, 2)} Mbps"),
                "Upload:" : str(f"{round(speed.upload() / 1_000_000, 2)} Mbps"),
                "Total Bytes Sent": self.get_size(net_io.bytes_sent),
                "Total Bytes Received": self.get_size(net_io.bytes_recv)
        }
        return data


    def __str__(self):
        return str("Returns a dictionary of system details; System, Boot Time, CPU, RAM, Network Speeds & Data Sent & Received, and GPU")


if __name__ == "__main__":
    scan = SystemScanner()
    menu = {
        1: scan.system_info,
        2: scan.cpu_info,
        3: scan.ram_info,
        4: scan.gpu_info,
        5: scan.disk_info,
        6: scan.network_info
    }
    while True:
        os.system("cls")
        print(f"\n[ SYSTEM SCANNER ]\n\n"
            "[0] Exit\n"
            "[1] System Information\n"
            "[2] Central Processing Unit\n"
            "[3] Random Access Memory\n"
            "[4] Graphical Processing Unit\n"
            "[5] Disk Information\n"
            "[6] Network Information\n\n")
        try:
            selection = int(input("  >> "))
            if selection == 0:
                os.system("cls")
                print("\nThank you for using the app! Have a nice day...\n\n")
                _ = input("Press Enter to exit..")
                break

            os.system("cls")
            choice = menu[selection]

            for key, value in choice().items():
                print(f"| {key:25}| {value}".ljust(5))
            print("\n")
            _ = input("Press Enter to continue..")
            continue 
        except:
            os.system("cls")
            print("\nInvalid input! Try again..\n\n")
            _ = input("Press Enter to continue..")
            continue

