#!/usr/bin/env bash

#SBATCH --time=00:10:25
#SBATCH --job-name="timing"
#SBATCH --cluster=smp
#SBATCH --partition=smp
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --ntasks=1
#SBATCH --output=out.txt
#SBATCH --mail-type=ALL
#SBATCH --mail-user=rbf12@pitt.edu

wget -nc -i url-list.txt -P data
