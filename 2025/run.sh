#! /bin/bash

gfortran -c utils.f90
gfortran $1 utils.o && ./a.out $2
