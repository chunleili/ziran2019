import subprocess
import os

current_path = os.path.dirname(os.path.abspath(__file__))

os.chdir(current_path)

case_number_list = [7]

for case_number in case_number_list:
    print('Running case ' + str(case_number))
    runCommand = './admm -test ' + str(case_number)
    subprocess.call([runCommand], shell=True)