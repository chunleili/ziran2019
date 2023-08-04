import subprocess

case_number_list = [1, 2, 3, 4, 5, 6]

for case_number in case_number_list:
    print('Running case ' + str(case_number))
    runCommand = './admm -test ' + str(case_number)
    subprocess.call([runCommand], shell=True)