import subprocess

import re

from tkinter import *


root = Tk()


root.title('Проверка температуры')

root.geometry('300x250')

# Define the PowerShell executable and command
ps_executable = r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
ps_command = "get-wmiobject msacpi_thermalzonetemperature -namespace 'root/wmi'"

# Combine the PowerShell executable and command into a single command
command = [ps_executable, '-Command', ps_command]

# Use subprocess.check_output to execute the command and capture its output
output = subprocess.check_output(command, text=True, stderr=subprocess.STDOUT)
pattern = r'CurrentTemperature\s+:\s+(\d+)'

# Search for the temperature value using the pattern
match = re.search(pattern, output)

current_temperature = match.group(1)

summ = int((int(current_temperature) / 10) - 273.15)

down_label = Label(root, text='Температура CPU', font=("Comic Sans MS", 22))
down_label.place(relx=0.5, rely=0.2, anchor=CENTER)

down_label = Label(root, text=summ, font=("Comic Sans MS", 24))
down_label.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
