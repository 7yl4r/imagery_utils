#!/bin/bash

#PBS -l walltime=20:00:00,nodes=rookery-0-05:ppn=2
#PBS -m n
#PBS -k oe
#PBS -j oe

cd $PBS_O_WORKDIR

echo $PBS_JOBID
echo $PBS_O_HOST
echo $PBS_NODEFILE
echo $a1

module load gdal/1.11.1

echo $p1
python $p1
