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
        net_io = psutil.net_io_counters()
        speed = speedtest.Speedtest()
        data = {
            "Interface": str(interfaces[0]),
            "Download": str(f"{round(speed.download() / 1_000_000, 2)} Mbps"),
            "Upload": str(f"{round(speed.upload() / 1_000_000, 2)} Mbps"),
            "Total Bytes Sent": str(self.get_size(net_io.bytes_sent)),
            "Total Bytes Received": str(self.get_size(net_io.bytes_recv))
        }
        return data



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
        tabControl.configure(width=500, height=300)

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

        self.style = ttk.Style(frame)
        self.style.configure("My.TLabel", font=("Arial", 12, "bold"))
        self.style.configure("Bold.TLabel", font=("Arial", 10, "bold"))
        self.style.configure("Title.TLabel", font=("Arial", 15, "bold"))
        

        self.widgets()

    def widgets(self):
        # System Tab
        system_label_frame = LabelFrame(self.system_tab, width=480, height=300)
        system_label_frame.grid(column=0, row=0)
        system_label_frame.grid_propagate(0)

        system_top_label = Label(system_label_frame, text="[ SYSTEM SPECIFICATIONS ]", style="Title.TLabel")
        system_top_label.grid(column=1, row=0, sticky=W, padx=30, pady=10)

        system_label = Label(system_label_frame, text="System: ", style="My.TLabel")
        system_label.grid(column=0, row=1, sticky=W)
        system_spec = Label(system_label_frame, text=self.methods["system"]["System"], style="Bold.TLabel")
        system_spec.grid(column=1, row=1, sticky=W, padx=10, pady=2)

        node_label = Label(system_label_frame, text="Node Name: ", style="My.TLabel")
        node_label.grid(column=0, row=2, sticky=W)
        node_spec = Label(system_label_frame, text=self.methods["system"]["Node Name"], style="Bold.TLabel")
        node_spec.grid(column=1, row=2, sticky=W, padx=10, pady=2)
        
        release_label = Label(system_label_frame, text="Release: ", style="My.TLabel")
        release_label.grid(column=0, row=3, sticky=W)
        release_spec = Label(system_label_frame, text=self.methods["system"]["Release"], style="Bold.TLabel")
        release_spec.grid(column=1, row=3, sticky=W, padx=10, pady=2)

        version_label = Label(system_label_frame, text="Version: ", style="My.TLabel")
        version_label.grid(column=0, row=4, sticky=W)
        version_spec = Label(system_label_frame, text=self.methods["system"]["Version"], style="Bold.TLabel")
        version_spec.grid(column=1, row=4, sticky=W, padx=10, pady=2)

        architecture_label = Label(system_label_frame, text="Architecture: ", style="My.TLabel")
        architecture_label.grid(column=0, row=5, sticky=W)
        architecture_spec = Label(system_label_frame, text=self.methods["system"]["Architecture"], style="Bold.TLabel")
        architecture_spec.grid(column=1, row=5, sticky=W, padx=10, pady=2)

        processor_label = Label(system_label_frame, text="Processor: ", style="My.TLabel")
        processor_label.grid(column=0, row=6, sticky=W)
        processor_spec = Label(system_label_frame, text=self.methods["system"]["Processor"], style="Bold.TLabel")
        processor_spec.grid(column=1, row=6, sticky=W, padx=10, pady=2)

        boot_label = Label(system_label_frame, text="Boot Time: ", style="My.TLabel")
        boot_label.grid(column=0, row=7, sticky=W)
        boot_spec = Label(system_label_frame, text=self.methods["system"]["Boot Time"], style="Bold.TLabel")
        boot_spec.grid(column=1, row=7, sticky=W, padx=10, pady=2)


        # Central Processing Unit Tab
        cpu_label_frame = LabelFrame(self.cpu_tab, width=480, height=300)
        cpu_label_frame.grid(column=0, row=0)
        cpu_label_frame.grid_propagate(0)

        cpu_top_label = Label(cpu_label_frame, text="[ CENTRAL PROCESSING UNIT ]", style="Title.TLabel")
        cpu_top_label.grid(column=1, row=0, sticky=W, padx=30, pady=10)

        cpu_core_label = Label(cpu_label_frame, text="Physical Cores: ")
        cpu_core_label.grid(column=0, row=1, sticky=W)
        cpu_core_spec = Label(cpu_label_frame, text=self.methods["cpu"]["Physical Cores"])
        cpu_core_spec.grid(column=1, row=1, sticky=W, padx=10)

        cpu_total_label = Label(cpu_label_frame, text="Total Cores: ")
        cpu_total_label.grid(column=0, row=2, sticky=W)
        cpu_total_spec = Label(cpu_label_frame, text=self.methods["cpu"]["Total Cores"])
        cpu_total_spec.grid(column=1, row=2, sticky=W, padx=10)
        
        cpu_max_label = Label(cpu_label_frame, text="Max Frequency: ")
        cpu_max_label.grid(column=0, row=3, sticky=W)
        cpu_max_spec = Label(cpu_label_frame, text=self.methods["cpu"]["Max Frequency"])
        cpu_max_spec.grid(column=1, row=3, sticky=W, padx=10)

        cpu_min_label = Label(cpu_label_frame, text="Min Frequency: ")
        cpu_min_label.grid(column=0, row=4, sticky=W)
        cpu_min_spec = Label(cpu_label_frame, text=self.methods["cpu"]["Min Frequency"])
        cpu_min_spec.grid(column=1, row=4, sticky=W, padx=10)

        cpu_cur_label = Label(cpu_label_frame, text="Current Frequency: ")
        cpu_cur_label.grid(column=0, row=5, sticky=W)
        cpu_cur_spec = Label(cpu_label_frame, text=self.methods["cpu"]["Current Frequency"])
        cpu_cur_spec.grid(column=1, row=5, sticky=W, padx=10)

        cpu_t_usage_label = Label(cpu_label_frame, text="Total Usage: ")
        cpu_t_usage_label.grid(column=0, row=6, sticky=W)
        cpu_t_usage_spec = Label(cpu_label_frame, text=self.methods["cpu"]["Total Usage"])
        cpu_t_usage_spec.grid(column=1, row=6, sticky=W, padx=10)


        # Random Access Memory Tab
        ram_label_frame = LabelFrame(self.ram_tab, width=480, height=300)
        ram_label_frame.grid(column=0, row=0)
        ram_label_frame.grid_propagate(0)

        ram_top_label = Label(ram_label_frame, text="[ RANDOM ACCESS MEMORY ]", style="Title.TLabel")
        ram_top_label.grid(column=1, row=0, sticky=W, padx=30, pady=10)

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


        # Graphics Processing Unit Tab
        gpu_label_frame = LabelFrame(self.gpu_tab, width=480, height=300)
        gpu_label_frame.grid(column=0, row=0)
        gpu_label_frame.grid_propagate(0)

        gpu_top_label = Label(gpu_label_frame, text="[ GRAPHICS PROCESSING UNIT ]", style="Title.TLabel")
        gpu_top_label.grid(column=1, row=0, sticky=W, padx=30, pady=10)

        gpu_id_label = Label(gpu_label_frame, text="ID: ")
        gpu_id_label.grid(column=0, row=1, sticky=W)
        gpu_id_spec = Label(gpu_label_frame, text=self.methods["gpu"]["ID"])
        gpu_id_spec.grid(column=1, row=1, sticky=W, padx=10)

        gpu_name_label = Label(gpu_label_frame, text="Name: ")
        gpu_name_label.grid(column=0, row=2, sticky=W)
        gpu_name_spec = Label(gpu_label_frame, text=self.methods["gpu"]["Name"])
        gpu_name_spec.grid(column=1, row=2, sticky=W, padx=10)
        
        gpu_load_label = Label(gpu_label_frame, text="Load: ")
        gpu_load_label.grid(column=0, row=3, sticky=W)
        gpu_load_spec = Label(gpu_label_frame, text=self.methods["gpu"]["Load"])
        gpu_load_spec.grid(column=1, row=3, sticky=W, padx=10)

        gpu_free_label = Label(gpu_label_frame, text="Free: ")
        gpu_free_label.grid(column=0, row=4, sticky=W)
        gpu_free_spec = Label(gpu_label_frame, text=self.methods["gpu"]["Free"])
        gpu_free_spec.grid(column=1, row=4, sticky=W, padx=10)

        gpu_used_label = Label(gpu_label_frame, text="Used: ")
        gpu_used_label.grid(column=0, row=5, sticky=W)
        gpu_used_spec = Label(gpu_label_frame, text=self.methods["gpu"]["Used"])
        gpu_used_spec.grid(column=1, row=5, sticky=W, padx=10)

        gpu_total_label = Label(gpu_label_frame, text="Total: ")
        gpu_total_label.grid(column=0, row=6, sticky=W)
        gpu_total_spec = Label(gpu_label_frame, text=self.methods["gpu"]["Total"])
        gpu_total_spec.grid(column=1, row=6, sticky=W, padx=10)

        gpu_temp_label = Label(gpu_label_frame, text="Temp: ")
        gpu_temp_label.grid(column=0, row=7, sticky=W)
        gpu_temp_spec = Label(gpu_label_frame, text=self.methods["gpu"]["Temp"])
        gpu_temp_spec.grid(column=1, row=7, sticky=W, padx=10)

        gpu_uuid_label = Label(gpu_label_frame, text="UUID: ")
        gpu_uuid_label.grid(column=0, row=8, sticky=W)
        gpu_uuid_spec = Label(gpu_label_frame, text=self.methods["gpu"]["UUID"])
        gpu_uuid_spec.grid(column=1, row=8, sticky=W, padx=10)


        # Disk Tab
        disk_label_frame = LabelFrame(self.disk_tab, width=480, height=300)
        disk_label_frame.grid(column=0, row=0)
        disk_label_frame.grid_propagate(0)

        disk_top_label = Label(disk_label_frame, text="[ DISK ]", style="Title.TLabel")
        disk_top_label.grid(column=1, row=0, sticky=W, padx=30, pady=10)

        disk_device_label = Label(disk_label_frame, text="Device: ")
        disk_device_label.grid(column=0, row=1, sticky=W)
        disk_device_spec = Label(disk_label_frame, text=self.methods["disk"]["Device"])
        disk_device_spec.grid(column=1, row=1, sticky=W, padx=10)

        disk_mount_label = Label(disk_label_frame, text="Mountpoint: ")
        disk_mount_label.grid(column=0, row=2, sticky=W)
        disk_mount_spec = Label(disk_label_frame, text=self.methods["disk"]["Mountpoint"])
        disk_mount_spec.grid(column=1, row=2, sticky=W, padx=10)
        
        disk_fs_label = Label(disk_label_frame, text="Filesystem: ")
        disk_fs_label.grid(column=0, row=3, sticky=W)
        disk_fs_spec = Label(disk_label_frame, text=self.methods["disk"]["Filesystem"])
        disk_fs_spec.grid(column=1, row=3, sticky=W, padx=10)

        disk_t_size_label = Label(disk_label_frame, text="Total Size: ")
        disk_t_size_label.grid(column=0, row=4, sticky=W)
        disk_t_size_spec = Label(disk_label_frame, text=self.methods["disk"]["Total Size"])
        disk_t_size_spec.grid(column=1, row=4, sticky=W, padx=10)

        disk_used_label = Label(disk_label_frame, text="Used: ")
        disk_used_label.grid(column=0, row=5, sticky=W)
        disk_used_spec = Label(disk_label_frame, text=self.methods["disk"]["Used"])
        disk_used_spec.grid(column=1, row=5, sticky=W, padx=10)

        disk_free_label = Label(disk_label_frame, text="Free: ")
        disk_free_label.grid(column=0, row=6, sticky=W)
        disk_free_spec = Label(disk_label_frame, text=self.methods["disk"]["Free"])
        disk_free_spec.grid(column=1, row=6, sticky=W, padx=10)

        disk_per_label = Label(disk_label_frame, text="Percentage: ")
        disk_per_label.grid(column=0, row=7, sticky=W)
        disk_per_spec = Label(disk_label_frame, text=self.methods["disk"]["Percentage"])
        disk_per_spec.grid(column=1, row=7, sticky=W, padx=10)

        disk_t_read_label = Label(disk_label_frame, text="Total Read: ")
        disk_t_read_label.grid(column=0, row=8, sticky=W)
        disk_t_read_spec = Label(disk_label_frame, text=self.methods["disk"]["Total Read"])
        disk_t_read_spec.grid(column=1, row=8, sticky=W, padx=10)

        disk_t_write_label = Label(disk_label_frame, text="Total Write: ")
        disk_t_write_label.grid(column=0, row=9, sticky=W)
        disk_t_write_spec = Label(disk_label_frame, text=self.methods["disk"]["Total Write"])
        disk_t_write_spec.grid(column=1, row=9, sticky=W, padx=10)


        # # Network Tab
        net_label_frame = LabelFrame(self.net_tab, width=480, height=300)
        net_label_frame.grid(column=0, row=0)
        net_label_frame.grid_propagate(0)

        net_top_label = Label(net_label_frame, text="[ NETWORK ]", style="Title.TLabel")
        net_top_label.grid(column=1, row=0, sticky=W, padx=30, pady=10)

        # net_interface_label = Label(net_label_frame, text="Interface: ")
        # net_interface_label.grid(column=0, row=0, sticky=W)
        # net_interface_spec = Label(net_label_frame, text=self.methods["net"]["Interface"])
        # net_interface_spec.grid(column=1, row=0, sticky=W, padx=10)

        # net_download_label = Label(net_label_frame, text="Download: ")
        # net_download_label.grid(column=0, row=1, sticky=W)
        # net_download_spec = Label(net_label_frame, text=self.methods["net"]["Download"])
        # net_download_spec.grid(column=1, row=1, sticky=W, padx=10)
        
        # net_upload_label = Label(net_label_frame, text="Upload: ")
        # net_upload_label.grid(column=0, row=2, sticky=W)
        # net_upload_spec = Label(net_label_frame, text=self.methods["net"]["Upload"])
        # net_upload_spec.grid(column=1, row=2, sticky=W, padx=10)

        # net_t_sent_label = Label(net_label_frame, text="Total Bytes Sent: ")
        # net_t_sent_label.grid(column=0, row=3, sticky=W)
        # net_t_sent_spec = Label(net_label_frame, text=self.methods["net"]["Total Bytes Sent"])
        # net_t_sent_spec.grid(column=1, row=3, sticky=W, padx=10)

        # net_t_recv_label = Label(net_label_frame, text="Total Bytes Received: ")
        # net_t_recv_label.grid(column=0, row=4, sticky=W)
        # net_t_recv_spec = Label(net_label_frame, text=self.methods["net"]["Total Bytes Received"])
        # net_t_recv_spec.grid(column=1, row=4, sticky=W, padx=10)


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
