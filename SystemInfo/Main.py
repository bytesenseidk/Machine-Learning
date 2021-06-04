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


class GUI(object):
    def __init__(self, master):
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
        label_frame = LabelFrame(self.first_tab, text="Label Frame", width=380, height=300)
        label_frame.grid(column=0, row=0)
        label_frame.grid_propagate(0)

        label = Label(label_frame, text="Label")
        label.grid(column=1, row=0)

        entry = Entry(label_frame, width=45)
        entry.grid(column=0, row=1, columnspan=3)
        entry.insert(0, "Entry field")

        radiobutton_1 = Radiobutton(label_frame, text="Radio 1", value=0)
        radiobutton_1.grid(column=0, row=2)
        radiobutton_2 = Radiobutton(label_frame, text="Radio 2", value=1)
        radiobutton_2.grid(column=1, row=2)
        checkbutton = Checkbutton(label_frame, text="Check")
        checkbutton.grid(column=2, row=2)

        button = Button(label_frame, text="Button")
        button.grid(column=0, row=3)

        menubutton = Menubutton(label_frame, text="Menu Button")
        menubutton.grid(column=1, row=3)
        menubutton.menu = Menu(menubutton, tearoff=0)
        menubutton["menu"] =  menubutton.menu
        menubutton.menu.add_checkbutton(label="first", variable=None)
        menubutton.menu.add_checkbutton(label="last", variable=None)

        scale = Scale(label_frame, from_=0, to=100, orient=HORIZONTAL)
        scale.grid(column=0, row=4)

        scrollbar = Scrollbar(label_frame)
        scrollbar.grid(column=2, row=4)

        list = Listbox(label_frame, yscrollcommand=scrollbar.set, height=5)
        for line in range(5):
            list.insert(END, "Listbox Element " + str(line))
        list.grid(column=2, row=4)
        scrollbar.config(command=list.yview)
        
        optionmenu = OptionMenu(label_frame, self.option, *self.options)
        optionmenu.grid(column=0, row=5)

        combobox = ttk.Combobox(label_frame, values=self.options)
        combobox.grid(column=1, row=5)
        combobox.current(0)

        progress = Progressbar(label_frame, orient=HORIZONTAL, length=100, mode='determinate')
        progress["value"] = 25
        progress.grid(column=2, row=5)

        treeview = ttk.Treeview(self.second_tab)
        treeview["columns"] = ("1","2","3")
        treeview.column("1", width=25)
        treeview.column("2", width=25)
        treeview.column("3", width=25)
        treeview.heading("1", text ="first") 
        treeview.heading("2", text ="second") 
        treeview.heading("3", text ="third")
        treeview.insert("", 'end', text ="Row 1", values=("Tree", "_", "View")) 
        treeview.insert("", 'end', text ="Row 2", values=("Tree", "_", "View")) 
        treeview.insert("", 'end', text ="Row 3", values=("Tree", "_", "View"))
        treeview.grid(column=0, row=0)
        treeview.grid_propagate(0)




if __name__ == "__main__":
    root = Tk()
    root.title("Tkinter Demo")
    Demo(root)
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
