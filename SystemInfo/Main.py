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
        data = {
            "System":       uname.system,   # Windows
            "Node Name":    uname.node,     # DESKTOP-NJHM05A
            "Release":      uname.release,  # 10
            "Version":      uname.version,  # 10.0.19041
            "architecture": uname.machine,  # AMD64
            "Processor":    uname.processor # Intel64 Family 6 Model 60 Stepping 3, GenuineIntel
        }
        return data


    def boot_time(self):
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        data = {"Boot Time": str(f"{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")}
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


    def network_flow(self):
        net_io = psutil.net_io_counters()
        data = {
            "Total Bytes Sent": self.get_size(net_io.bytes_sent),
            "Total Bytes Received": self.get_size(net_io.bytes_recv)
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
            data["Temperature"] = f"{gpu.temperature} °C"
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
    

    def __str__(self):
        return str("Returns a dictionary of system details; System, Boot Time, CPU, RAM, Data Sent and Received, & GPU")


class Network_Details(object):
    def __init__(self):
        self.scanner = psutil.net_if_addrs()
        self.speed = speedtest.Speedtest()
        self.interfaces = self.interface()[0]

    def interface(self):
        interfaces = []
        for interface_name, _ in self.scanner.items():
            interfaces.append(str(interface_name))
        return interfaces

    def scan(self):
        data = {"Interface:" : self.interfaces,
                "Download:" : str(f"{round(self.speed.download() / 1_000_000, 2)} Mbps"),
                "Upload:" : str(f"{round(self.speed.upload() / 1_000_000, 2)} Mbps")
        }
        return data

    def __str__(self):
        return str("Returns a dictionary of network details; Interface, Download Speed & Upload Speed")



if __name__ == "__main__":
    scan = SystemScanner()
    net = Network_Details()
    print(f"""
    {scan.system_info()}
    {scan.boot_time()}
    {scan.cpu_info()}
    {scan.ram_info()}
    {scan.network_flow()}
    {scan.gpu_info()}
    {scan.disk_info()}
    {net.scan()}
    """)
