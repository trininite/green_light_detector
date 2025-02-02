import os

current_path = os.getcwd()

while ".WDM" not in os.listdir(current_path):
    os.chdir("..")
    current_path = os.getcwd()

print(current_path)