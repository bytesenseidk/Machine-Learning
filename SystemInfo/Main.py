import GPUtil
import psutil
import platform
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
        return str(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")


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


def gpu_info():
    gpus = GPUtil.getGPUs()
    data = []
    gpu_list = {}
    for gpu in gpus:
        gpu_list["ID"] = gpu.id
        gpu_list["Name"] = gpu.name
        gpu_list["Load"] = f"{gpu.load*100}%"
        gpu_list["Free"] = f"{gpu.memoryFree}MB"
        gpu_list["Used"] = f"{gpu.memoryUsed}MB"
        gpu_list["Total"] = f"{gpu.memoryTotal}MB"
        gpu_list["Temperature"] = f"{gpu.temperature} °C"
        gpu_list["UUID"] = gpu.uuid
        data.append(gpu_list)
    return data
    
# system_info()
# boot_time()
# print(cpu_info())
# cpu_info()


# ram_info()
# disk_info()
# network_info()
print(gpu_info())



""" TODO
    def disk_info(self):
        partitions = psutil.disk_partitions()
        data = {

        }
        for partition in partitions:
            print(f"=== Device: {partition.device} ===")
            print(f"  Mountpoint: {partition.mountpoint}")
            print(f"  File system type: {partition.fstype}")
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                # this can be catched due to the disk that
                # isn't ready
                continue
            print(f"  Total Size: {get_size(partition_usage.total)}")
            print(f"  Used: {get_size(partition_usage.used)}")
            print(f"  Free: {get_size(partition_usage.free)}")
            print(f"  Percentage: {partition_usage.percent}%")
        # get IO statistics since boot
        disk_io = psutil.disk_io_counters()
        print(f"Total read: {get_size(disk_io.read_bytes)}")
        print(f"Total write: {get_size(disk_io.write_bytes)}")

Network details
"""








# import psutil
# import platform
# from datetime import datetime

# """ Scale large byte sizes """
# def get_size(bytes, suffix="B"):
#     factor = 1024   # bytes
#     for unit in ["", "K", "M", "G", "T", "P"]:
#         # Checks if it's above a KB.
#         if bytes < factor:
#             return f"{bytes:.2f}{unit}{suffix}"
#         # Byte conversion
#         bytes /= factor


# def system_informations():
#     print("="*40, "System Information", "="*40)
#     uname = platform.uname()
#     print(f"System: {uname.system}")
#     print(f"Node Name: {uname.node}")
#     print(f"Release: {uname.release}")
#     print(f"Version: {uname.version}")
#     print(f"Machine: {uname.machine}")
#     print(f"Processor: {uname.processor}")

# def boot_time():
#     print("="*40, "Boot Time", "="*40)
#     boot_time_timestamp = psutil.boot_time()
#     bt = datetime.fromtimestamp(boot_time_timestamp)
#     print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")


# def cpu_info():
#     print("="*40, "Central Processing Unit", "="*40)
#     # Amount of cores
#     print("Physical cores: ", psutil.cpu_count(logical=False))
#     print("Total cores: ", psutil.cpu_count(logical=True))
#     # Frequencies
#     cpufreq = psutil.cpu_freq()
#     print(f"Max frequency: {cpufreq.max:.2f}Mhz")
#     print(f"Min frequency: {cpufreq.min:.2f}Mhz")
#     print(f"Current frequency: {cpufreq.current:.2f}Mhz")
#     # Usage
#     print("CPU Usage Per Core:")
#     for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
#         print(f"Core {i}: {percentage}%")
#     print(f"Total CPU Usage: {psutil.cpu_percent()}%")

# if __name__ == "__main__":
#     system_informations()
#     boot_time()
#     cpu_info()

