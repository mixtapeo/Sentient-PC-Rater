import platform
import GPUtil
import psutil
import wmi
import cpuinfo
import tkinter
import pandas as pd
from pathlib import Path
from pathlib import Path
from tkinter import Tk, Canvas
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import *
from PIL import ImageTk, Image
from PIL import Image, ImageTk
from typing import Any
from tabulate import tabulate


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            # noinspection PyCompatibility
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


my_system = platform.uname()

# printing info
print(f"CPU: {cpuinfo.get_cpu_info()['brand_raw']}")
print(f"System: {my_system.system}")
svmem = psutil.virtual_memory()
print(f"Memory: {get_size(svmem.total)}")
c = wmi.WMI()
my_system = c.Win32_ComputerSystem()[0]
print(f"Motherboard: {my_system.Model}")
print(f"System Type: {my_system.SystemType}")
# print(f"Manufacturer: {my_system.Manufacturer}")
# print(f"Machine: {my_system.machine}")
# (f"Processor: {my_system.processor}")
# print(f"Release: {my_system.release}")

gpus = GPUtil.getGPUs()
list_gpus = []
for gpu in gpus:
    # get the GPU id
    gpu_id = gpu.id
    # name of GPU
    gpu_name = gpu.name
    # get % percentage of GPU usage of that GPU
    gpu_load = f"{gpu.load * 100}%"
    # get free memory in MB format
    # gpu_free_memory = f"{gpu.memoryFree}MB"
    # get used memory
    gpu_used_memory = f"{gpu.memoryUsed}MB"
    # get total memory
    gpu_total_memory = f"{gpu.memoryTotal}MB"
    # get GPU temperature in Celsius
    # gpu_temperature = f"{gpu.temperature} °C"
    # gpu_uuid = gpu.uuid
    list_gpus.append((
        gpu_id, gpu_name,  # gpu_load, gpu_free_memory, gpu_used_memory,
        gpu_total_memory,  # gpu_temperature, #gpu_uuid
    ))

print(tabulate(list_gpus, headers=("id", "name", "load", "free memory", "used memory", "total memory",
                                   "temperature", "uuid")))
# importing benchmarked hardware spreadsheets, CPU
# workbook = pd.read_csv('CPU_UserBenchmarks.csv')
# print(workbook['Rank'].iloc[0])
# workbook.head()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# rating algorithm
x = float(svmem.total / 1000000000)
b = float(1.7)
c = float(3.0)
d = float(7)
e = float(15)
f = float(23)
g = float(30)
if x > g:
    exec(open("guivariation (6).py").read())
elif x > f:
    exec(open("guivariation (5).py").read())
elif x > e:
    exec(open("guivariation (4).py").read())
elif x > d:
    exec(open("guivariation (3).py").read())
elif x > c:
    exec(open("guivariation (2).py").read())
else:
    exec(open("guivariation (1).py").read())

