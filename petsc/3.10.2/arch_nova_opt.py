#!/usr/bin/env python

import os

configure_options = [
  '--with-debugging=0',
  '--with-clanguage=cxx',
  '--with-x=0',
  '--with-fc=mpiifort',
  '--with-cc=mpiicc',
  'F90=$F90',
  'F77=$F77',
  '--with-cxx=mpiicpc',
  '--download-mumps=1',
  '--download-blacs=1',
  '--download-scalapack=1',
  '--download-metis=1',
  '--download-fblaslapack=1',
  '--download-parmetis=1',
  'COPTFLAGS=-O3 -xHost',
  'CXXOPTFLAGS=-O3 -xHost',
  'FOPTFLAGS=-O3 -xHost',
  ]

if __name__ == '__main__':
  import sys,os
  sys.path.insert(0,os.path.abspath('config'))
  import configure
  configure.petsc_configure(configure_options)
