# import psutil
# import platform
# import platform
# import GPUtil
# import psutil
# import wmi
# import cpuinfo
# import tkinter
# import pandas as pd
# from pathlib import Path
# from pathlib import Path
# from tkinter import Tk, Canvas
# from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
# from tkinter import *
# from PIL import ImageTk, Image
# from PIL import Image, ImageTk
# from typing import Any
# from tabulate import tabulate
# # # from datetime import datetime
# # #
# # # def get_size(bytes, suffix="B"):
# # #     """
# # #     Scale bytes to its proper format
# # #     e.g:
# # #         1253656 => '1.20MB'
# # #         1253656678 => '1.17GB'
# # #     """
# # #     factor = 1024
# # #     for unit in ["", "K", "M", "G", "T", "P"]:
# # #         if bytes < factor:
# # #             return f"{bytes:.2f}{unit}{suffix}"
# # #         bytes /= factor
# # #
# # #
# # # # let's print CPU information
# # # print("="*40, "CPU Info", "="*40)
# # # # number of cores
# # # print("Physical cores:", psutil.cpu_count(logical=False))
# # # print("Total cores:", psutil.cpu_count(logical=True))
# # # # CPU frequencies
# # # cpufreq = psutil.cpu_freq()
# # # print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
# # # print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
# # # print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
# # # # CPU usage
# # # print("CPU Usage Per Core:")
# # # for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
# # #     print(f"Core {i}: {percentage}%")
# # # print(f"Total CPU Usage: {psutil.cpu_percent()}%")
# # #
# # # # Memory Information
# # # print("="*40, "Memory Information", "="*40)
# # # # get the memory details
# # # svmem = psutil.virtual_memory()
# # # print(f"Total: {get_size(svmem.total)}")
# # # print(f"Available: {get_size(svmem.available)}")
# # # print(f"Used: {get_size(svmem.used)}")
# # # print(f"Percentage: {svmem.percent}%")
# # # print("="*20, "SWAP", "="*20)
# # # # get the swap memory details (if exists)
# # # swap = psutil.swap_memory()
# # # print(f"Total: {get_size(swap.total)}")
# # # print(f"Free: {get_size(swap.free)}")
# # # print(f"Used: {get_size(swap.used)}")
# # # print(f"Percentage: {swap.percent}%")
# #
# #
# # # import cpuinfo
# # # print(cpuinfo.get_cpu_info()['brand_raw'])
# # # import tkinter
# # # from tkinter import *
# # # from PIL import Image, ImageTk
# # #
# # # root = Tk()
# # #
# # # # Create a photoimage object of the image in the path
# # # image1 = Image.open("assets/tick.jpg")
# # # test = ImageTk.PhotoImage(image1)
# # #
# # # label1 = tkinter.Label(image=test)
# # # label1.image = test
# # #
# # # # Position image
# # # label1.place(x=4, y=7)
# # # root.mainloop()
# #
# # import platform
# # import GPUtil
# # import psutil
# # import wmi
# # from tabulate import tabulate
# # from pathlib import Path
# # from tkinter import Tk, Canvas
# # import cpuinfo
# # from pathlib import Path
# # from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
# # import pandas as pd
# # from PIL import ImageTk, Image
# # import tkinter
# # from tkinter import *
# # from PIL import Image, ImageTk
# #
# # def get_size(bytes, suffix="B"):
# #     """
# #     Scale bytes to its proper format
# #     e.g:
# #         1253656 => '1.20MB'
# #         1253656678 => '1.17GB'
# #     """
# #     factor = 1024
# #     for unit in ["", "K", "M", "G", "T", "P"]:
# #         if bytes < factor:
# #             # noinspection PyCompatibility
# #             return f"{bytes:.2f}{unit}{suffix}"
# #         bytes /= factor
# #
# #
# # my_system = platform.uname()
# #
# # # printing info
# # # noinspection PyCompatibility
# # print(f"CPU: {cpuinfo.get_cpu_info()['brand_raw']}")
# # print(f"System: {my_system.system}")
# # # print(f"Release: {my_system.release}")
# # svmem = psutil.virtual_memory()
# # print(f"Memory: {get_size(svmem.total)}")
# # # print(f"Machine: {my_system.machine}")
# # # (f"Processor: {my_system.processor}")
# # c = wmi.WMI()
# # my_system = c.Win32_ComputerSystem()[0]
# # # print(f"Manufacturer: {my_system.Manufacturer}")
# # print(f"Motherboard: {my_system.Model}")
# # print(f"System Type: {my_system.SystemType}")
# #
# # gpus = GPUtil.getGPUs()
# # list_gpus = []
# # for gpu in gpus:
# #     # get the GPU id
# #     gpu_id = gpu.id
# #     # name of GPU
# #     gpu_name = gpu.name
# #     # get % percentage of GPU usage of that GPU
# #     gpu_load = f"{gpu.load * 100}%"
# #     # get free memory in MB format
# #     # gpu_free_memory = f"{gpu.memoryFree}MB"
# #     # get used memory
# #     gpu_used_memory = f"{gpu.memoryUsed}MB"
# #     # get total memory
# #     gpu_total_memory = f"{gpu.memoryTotal}MB"
# #     # get GPU temperature in Celsius
# #     # gpu_temperature = f"{gpu.temperature} °C"
# #     # gpu_uuid = gpu.uuid
# #     list_gpus.append((
# #         gpu_id, gpu_name,  # gpu_load, gpu_free_memory, gpu_used_memory,
# #         gpu_total_memory,  # gpu_temperature, #gpu_uuid
# #     ))
# # # gui window
# # OUTPUT_PATH = Path(__file__).parent
# # ASSETS_PATH = OUTPUT_PATH / Path("./assets")
# # def relative_to_assets(path: str) -> Path:
# #     return ASSETS_PATH / Path(path)
# # window = Tk()
# # window.lift()
# # window.attributes("-topmost", True)
# # window.geometry("1000x600")
# # window.configure(bg="#DD5D5D")
# # root = window
# # root.iconbitmap("assets/tick.ico")
# # root.title('intelligent program')
# # # Place my_widget in grid at 1,2
# # my_widget.grid(row = 1, column = 2)
# #
# # # Hide my_widget but remember where it was
# # my_widget.grid_remove()
# #
# # # Un-hide my_widget, restoring it to where it was (1,2)
# # my_widget.grid()
#
# #rating algorithm
# #ram
#
#
# def get_size(bytes, suffix="B"):
#     """
#     Scale bytes to its proper format
#     e.g:
#         1253656 => '1.20MB'
#         1253656678 => '1.17GB'
#     """
#     factor = 1024
#     for unit in ["", "K", "M", "G", "T", "P"]:
#         if bytes < factor:
#             # noinspection PyCompatibility
#             return f"{bytes:.2f}{unit}{suffix}"
#         bytes /= factor
#
# svmem = psutil.virtual_memory()
#
# a = svmem.total
# b = 2
# c = 4
# d = 8
# e = 16
# f = 24
# g = 32
#
# if b: exec(open("guivariation (1).py").read())
# if c: exec(open("guivariation (2).py").read())
# if d: exec(open("guivariation (3).py").read())
# if e: exec(open("guivariation (4).py").read())
# if f: exec(open("guivariation (5).py").read())
# if g: exec(open("guivariation (6).py").read())
