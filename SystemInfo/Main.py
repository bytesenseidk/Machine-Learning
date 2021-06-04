import GPUtil
import psutil
import platform
import speedtest
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
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
                return f"{bytes:.2f} {unit}{suffix}"
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
            "Architecture": uname.machine,
            "Processor":    uname.processor,
            "Boot Time": str(f"{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
        }
        return data


    def cpu_info(self):
        cpufreq = psutil.cpu_freq()
        data = {
            "Physical Cores": psutil.cpu_count(logical=False),
            "Total Cores": psutil.cpu_count(logical=True),
            "Max Frequency": str(f"{cpufreq.max:.2f} Mhz"),
            "Min Frequency": str(f"{cpufreq.min:.2f} Mhz"),
            "Current Frequency": str(f"{cpufreq.current:.2f} Mhz"),
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



class GUI(object):
    def __init__(self, master):
        spec = SystemScanner()
        self.methods = {
            "system": spec.system_info(),
            "cpu": spec.cpu_info(),
            "ram": spec.ram_info(),
            "gpu": spec.gpu_info(),
            "disk": spec.disk_info(),
            "net": spec.network_info
        }
        frame = Frame(master)
        frame.grid()
        tabControl = ttk.Notebook(root)
        tabControl.configure(width=400, height=300)

        self.system_tab = ttk.Frame(tabControl)
        tabControl.add(self.system_tab, text="System")
        tabControl.grid()

        self.cpu_tab = ttk.Frame(tabControl)
        tabControl.add(self.cpu_tab, text="CPU")
        tabControl.grid()

        self.ram_tab = ttk.Frame(tabControl)
        tabControl.add(self.ram_tab, text="RAM")
        tabControl.grid()

        self.gpu_tab = ttk.Frame(tabControl)
        tabControl.add(self.gpu_tab, text="GPU")
        tabControl.grid()

        self.disk_tab = ttk.Frame(tabControl)
        tabControl.add(self.disk_tab, text="Disk")
        tabControl.grid()

        self.net_tab = ttk.Frame(tabControl)
        tabControl.add(self.net_tab, text="Network")
        tabControl.grid()

        self.widgets()

    def widgets(self):
        # System Tab
        system_label_frame = LabelFrame(self.system_tab, text="[ SYSTEM ]", width=380, height=300)
        system_label_frame.grid(column=0, row=0)
        system_label_frame.grid_propagate(0)

        system_label = Label(system_label_frame, text="System: ")
        system_label.grid(column=0, row=0, sticky=W)
        system_spec = Label(system_label_frame, text=self.methods["system"]["System"])
        system_spec.grid(column=1, row=0, sticky=W, padx=10)

        node_label = Label(system_label_frame, text="Node Name: ")
        node_label.grid(column=0, row=1, sticky=W)
        node_spec = Label(system_label_frame, text=self.methods["system"]["Node Name"])
        node_spec.grid(column=1, row=1, sticky=W, padx=10)
        
        release_label = Label(system_label_frame, text="Release: ")
        release_label.grid(column=0, row=2, sticky=W)
        release_spec = Label(system_label_frame, text=self.methods["system"]["Release"])
        release_spec.grid(column=1, row=2, sticky=W, padx=10)

        version_label = Label(system_label_frame, text="Version: ")
        version_label.grid(column=0, row=3, sticky=W)
        version_spec = Label(system_label_frame, text=self.methods["system"]["Version"])
        version_spec.grid(column=1, row=3, sticky=W, padx=10)

        architecture_label = Label(system_label_frame, text="Architecture: ")
        architecture_label.grid(column=0, row=4, sticky=W)
        architecture_spec = Label(system_label_frame, text=self.methods["system"]["Architecture"])
        architecture_spec.grid(column=1, row=4, sticky=W, padx=10)

        processor_label = Label(system_label_frame, text="Processor: ")
        processor_label.grid(column=0, row=5, sticky=W)
        processor_spec = Label(system_label_frame, text=self.methods["system"]["Processor"])
        processor_spec.grid(column=1, row=5, sticky=W, padx=10)

        boot_label = Label(system_label_frame, text="Boot Time: ")
        boot_label.grid(column=0, row=6, sticky=W)
        boot_spec = Label(system_label_frame, text=self.methods["system"]["Boot Time"])
        boot_spec.grid(column=1, row=6, sticky=W, padx=10)

        # Central Processing Unit Tab
        cpu_label_frame = LabelFrame(self.cpu_tab, text="[ CENTRAL PROCESSING UNIT ]", width=380, height=300)
        cpu_label_frame.grid(column=0, row=0)
        cpu_label_frame.grid_propagate(0)

        core_label = Label(cpu_label_frame, text="Physical Cores: ")
        core_label.grid(column=0, row=0, sticky=W)
        core_spec = Label(cpu_label_frame, text=self.methods["cpu"]["Physical Cores"])
        core_spec.grid(column=1, row=0, sticky=W, padx=10)

        total_label = Label(cpu_label_frame, text="Total Cores: ")
        total_label.grid(column=0, row=1, sticky=W)
        total_spec = Label(cpu_label_frame, text=self.methods["cpu"]["Total Cores"])
        total_spec.grid(column=1, row=1, sticky=W, padx=10)
        
        max_freq_label = Label(cpu_label_frame, text="Max Frequency: ")
        max_freq_label.grid(column=0, row=2, sticky=W)
        max_freq_spec = Label(cpu_label_frame, text=self.methods["cpu"]["Max Frequency"])
        max_freq_spec.grid(column=1, row=2, sticky=W, padx=10)

        min_freq_label = Label(cpu_label_frame, text="Min Frequency: ")
        min_freq_label.grid(column=0, row=3, sticky=W)
        min_freq_spec = Label(cpu_label_frame, text=self.methods["cpu"]["Min Frequency"])
        min_freq_spec.grid(column=1, row=3, sticky=W, padx=10)

        cur_freq_label = Label(cpu_label_frame, text="Current Frequency: ")
        cur_freq_label.grid(column=0, row=4, sticky=W)
        cur_freq_spec = Label(cpu_label_frame, text=self.methods["cpu"]["Current Frequency"])
        cur_freq_spec.grid(column=1, row=4, sticky=W, padx=10)

        total_usage_label = Label(cpu_label_frame, text="Total Usage: ")
        total_usage_label.grid(column=0, row=5, sticky=W)
        total_usage_spec = Label(system_label_frame, text=self.methods["cpu"]["Total Usage"])
        total_usage_spec.grid(column=1, row=5, sticky=W, padx=10)


        # Random Access Memory Tab
        ram_label_frame = LabelFrame(self.ram_tab, text="[ RANDOM ACCESS MEMORY ]", width=380, height=300)
        ram_label_frame.grid(column=0, row=0)
        ram_label_frame.grid_propagate(0)

        ram_total_label = Label(ram_label_frame, text="Total: ")
        ram_total_label.grid(column=0, row=0, sticky=W)
        ram_total_spec = Label(ram_label_frame, text=self.methods["ram"]["Total"])
        ram_total_spec.grid(column=1, row=0, sticky=W, padx=10)

        ram_avail_label = Label(ram_label_frame, text="Available: ")
        ram_avail_label.grid(column=0, row=1, sticky=W)
        ram_avail_spec = Label(ram_label_frame, text=self.methods["ram"]["Available"])
        ram_avail_spec.grid(column=1, row=1, sticky=W, padx=10)
        
        ram_used_label = Label(ram_label_frame, text="Used: ")
        ram_used_label.grid(column=0, row=2, sticky=W)
        ram_used_spec = Label(ram_label_frame, text=self.methods["ram"]["Used"])
        ram_used_spec.grid(column=1, row=2, sticky=W, padx=10)

        ram_per_label = Label(ram_label_frame, text="Percentage: ")
        ram_per_label.grid(column=0, row=3, sticky=W)
        ram_per_spec = Label(ram_label_frame, text=self.methods["ram"]["Percentage"])
        ram_per_spec.grid(column=1, row=3, sticky=W, padx=10)

if __name__ == "__main__":
    root = Tk()
    root.title("System Information")
    GUI(root)
    root.mainloop()


    # scan = SystemScanner()
    # menu = {
    #     1: scan.system_info,
    #     2: scan.cpu_info,
    #     3: scan.ram_info,
    #     4: scan.gpu_info,
    #     5: scan.disk_info,
    #     6: scan.network_info
    # }
    # while True:
    #     os.system("cls")
    #     print(f"\n[ SYSTEM SCANNER ]\n\n"
    #         "[0] Exit\n"
    #         "[1] System Information\n"
    #         "[2] Central Processing Unit\n"
    #         "[3] Random Access Memory\n"
    #         "[4] Graphical Processing Unit\n"
    #         "[5] Disk Information\n"
    #         "[6] Network Information\n\n")
    #     try:
    #         selection = int(input("  >> "))
    #         if selection == 0:
    #             os.system("cls")
    #             print("\nThank you for using the app! Have a nice day...\n\n")
    #             _ = input("Press Enter to exit..")
    #             break

    #         os.system("cls")
    #         choice = menu[selection]

    #         for key, value in choice().items():
    #             print(f"| {key:25}| {value}".ljust(5))
    #         print("\n")
    #         _ = input("Press Enter to continue..")
    #         continue 
    #     except:
    #         os.system("cls")
    #         print("\nInvalid input! Try again..\n\n")
    #         _ = input("Press Enter to continue..")
    #         continue
