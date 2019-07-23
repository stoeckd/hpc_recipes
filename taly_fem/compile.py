#!/usr/bin/env python

import socket
import os
import shutil
import subprocess

host = socket.gethostname()
print(host)
if host.startswith(('condo','cyence','nova')):
    CXX='mpiicpc'
    CC='mpiicc'
elif host.startswith(('bglab','comet')):
    CXX='mpicxx'
    CC='mpicc'
elif host.startswith('Dans'):
    CXX='mpicxx'
    CC='mpicc'

cmake_cmd = ("cmake "
"-Dtalyfem_DIR=${{FEMLIB_DIR}} "
"-DCMAKE_C_COMPILER={} "
"-DCMAKE_CXX_COMPILER={} "
"-DCMAKE_BUILD_TYPE=Release "
"-DCMAKE_CXX_FLAGS=\"-O3 -xHost -DNDEBUG\" ..".format(CC, CXX))

print(cmake_cmd)

if not os.path.exists('build_opt'):
    os.makedirs('build_opt')
elif os.path.exists('build_opt'):
    shutil.rmtree('build_opt')
    os.makedirs('build_opt')

os.chdir('build_opt')

print(cmake_cmd)
subprocess.call(cmake_cmd, shell=True)
subprocess.call('make -j 4', shell=True)

os.chdir('..')
