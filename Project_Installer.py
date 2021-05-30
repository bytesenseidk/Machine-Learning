import os
import platform

operating_system = platform.system()
commands = {
    "Windows": {"clean": "cls",
                "pip": "pip",
                "split": "\\",
                "env": "venv\\Scripts\\activate"
                },
    "Linux": {"clean": "clear", 
                "pip": "pip3",
                "split": "/",
                "env": "source venv/bin/activate"
                },
    "Mac": {"clean": "clear",
                "pip": "pip",
                "split": "/",
                "env": "source venv/bin/activate"
                }
}

project_path = input(r"[!] Drag 'n Drop Project Folder Here: ")
os.chdir(project_path)
project_name = os.getcwd().split(commands[operating_system]["split"])[-1]

""" Environment """
os.system(f"{commands[operating_system]['pip']} install virtualenv")

if not os.path.isdir("venv"):
    os.system("virtualenv venv")
os.system(commands[operating_system]["clean"])

""" Modules """
if os.path.isfile("requirements.txt"):
    print("\n[!] Will now install the following modules:\n")
    with open("requirements.txt", "r+") as modules:
        for module in modules.readlines():
            print(module.strip("\n"))
    print("\n")
    _ = input("[!] Press Enter to continue..")
    os.system(f"{commands[operating_system]['env']} && {commands[operating_system]['pip']} install -r requirements.txt")
else:
    print("\n[!] No requirements.txt file detected!\n")
    _ = input("[!] Press Enter to continue..")

os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.system(commands[operating_system]["clean"])

print("\nSetup is now complete..\n\n",
    f"[!] Project Name:           \"{project_name}\"\n",
    f"[!] Activate Environment:   \"{project_path}{commands[operating_system]['split']}{commands[operating_system]['env']}\"\n",
    f"[!] Deactivate Environment: \"deactivate\"\n\n")
