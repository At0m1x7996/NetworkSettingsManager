import sys
import subprocess

baseCommand = sys.executable + " -m pip install"
packages = ["WMI", "ctypes-windows"]

if __name__ == "__main__":
    for package in packages:
        command = (baseCommand + " " + package).split(" ")
        # implement pip as a subprocess:
        subprocess.check_call(command)