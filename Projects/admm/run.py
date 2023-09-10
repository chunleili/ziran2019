import subprocess
import os
import argparse

current_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_path)

parser = argparse.ArgumentParser()
parser.add_argument('-test', nargs='+', type=int, default=[6])
parser.add_argument('-restart_frame', type=int, default=-1)
args = parser.parse_args()
case_number_list = args.test
restart_frame = args.restart_frame

for case_number in case_number_list:
    print('Running case ' + str(case_number))
    if restart_frame >= 0:
        runCommand = './admm -test ' + str(case_number) + str(' -restart ') + str(restart_frame)
    else:
        runCommand = './admm -test ' + str(case_number)
    subprocess.call([runCommand], shell=True)