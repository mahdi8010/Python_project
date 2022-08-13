
import os


import subprocess

os.chdir("E:")

result = subprocess.check_output("dir /S /B *.xlsx",shell=True).decode().split()


for hadaf in result :
    os.remove(hadaf)
    print(" Removed : "+ hadaf)