# NEST GPU Dynamic Network Creation

This repository contains the data and scripts used for the #INSERT PAPER REF#.

## Requirements
To run the simulations, NEST GPU version #INSERT MAIN TAG# and version #INSERT CONN TAG#, NEST version 3.3, and GeNN version 4.8.0 are required.
For installation instructions on the simulators, see:
 - https://nest-gpu.readthedocs.io/en/latest/installation/index.html
 - https://nest-simulator.readthedocs.io/en/v3.3/installation/index.html
 - https://genn-team.github.io/genn/documentation/4/html/d8/d99/Installation.html

Additionally to run the scripts to post process the data and generate plots, Python and additional packages are required.
To run the data post processing scripts and plotting scripts the following software was used:
 * Python 3.8.6
 * Numpy 1.22
 * Matplotlib 3.5
 * Tol Colors 1.2.1 (https://pypi.org/project/tol-colors/)

## Contents
The [data](data/) directory contains all of the generated data used in the paper and the [plots](plots/) directory contains the scripts to generate the plots in the paper.

Simulation scripts to generate new datasets are found in [balanced_izh](balanced_izh/), [ngpu_microcircuit](ngpu_microcircuit/), [nest_microcircuit](nest_microcircuit/), [genn_microcircuit](genn_microcirctui/).

Simulation scripts directories prepended by:
 - ngpu_: are meant to be run with NEST GPU.
 - nest_: are meant to be run with NEST.
 - genn_: are meant to be run with GeNN.

 <br>

 The models available in this repository are:
  - Potjans & Diesmann cortical microcircuit for NEST GPU, NEST and GeNN
    - NEST GPU microcircuit taken from: https://github.com/nest/nest-gpu/tree/main/python/Potjans_2014
    - NEST microcircuit taken from: https://github.com/nest/nest-simulator/tree/master/pynest/examples/Potjans_2014
    - GeNN microcircuit taken from: https://github.com/BrainsOnBoard/pygenn_paper
  - Balanced random network with STDP synapses and Izhikevich neurons for NEST GPU

<br>

Each model directory contains additional benchmarking and data post processing scripts in order to automatically run simulations and gather the resulting data.
In particular:
 - ```run_benchmark.py```: Python script based on the original simulation script of the model with additional adaptations for benchmarking, notably the addition of command line argument handling, simulation timers (cf Models sub-section in #INSERT PAPER REF#), and data exporting to json files.
   - This Python script is meant to be run by the ```benchmark.sh``` script found in each model directory.
     - To run it individually, examples of local execution and SLURM execution are found in each corresponding ```benchmark.sh```.
   - As stated in the "Hardware and Software" subsection in #INSERT PAPER REF#, in these scripts:
     - Spike recording is disabled.
     - Poisson generators are enabled.
     - Optimized membrane potentials are enabled.
     - Presimulation runs for 0.1ms.
     - Simulation runs for 10s.
 - ```gather_data.py```: Python script designed to collect the data from all of the simulation runs of a benchmark and compute the mean values and the standard deviation of the simulation timers.
   - This Python script is meant to be run by the ```benchmark.sh``` script found in each model directory.
     - To run it individually, examples of local execution are found in each corresponding ```benchmark.sh```.
 - ```benchmark.sh```: Bash script to automatically benchmark the model with 10 different random generation seeds and collect the data.
   - Can be used to run locally or through SLURM with an interactive session.
     - By default, it is set to run locally. To change this, uncomment respective line execution line in script. More information can be found in the READMEs of each model directory.
     - SLURM executions assume a system equipped with 128, this can be changed through ```cores``` variable at the beginning of each script.

Individual instructions for each script are given in the respective model directories.


## TODOS:

 - rename balanced_izh directory to ngpu_balanced_izh
 - delete balanced_* directories if models not used for paper
 - add balanced_*/README.md
 