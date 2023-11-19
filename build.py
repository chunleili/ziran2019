import argparse
import os
import subprocess

# ## Building in Ziran

#     mkdir build && cd build
#     cmake .. -DCMAKE_BUILD_TYPE=Release
#     make -j 4
def build():
    project_path = os.path.dirname(os.path.realpath(__file__))

    # cd to project directory
    os.chdir(project_path)

    #check if build directory exists
    if not os.path.exists('build'):
        os.mkdir('build')
    # cd to build directory
    os.chdir('build')

    # verify current dir is build
    assert os.getcwd() == os.path.join(project_path, 'build')

    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true')

    if parser.parse_args().debug:
        subprocess.call(['cmake','..', '-DCMAKE_BUILD_TYPE=Debug'])
    else:
        subprocess.call(['cmake','..', '-DCMAKE_BUILD_TYPE=Release'])


    subprocess.call(['make', '-j', '16'])

    print('Build complete')

if __name__ == "__main__":
    build()
