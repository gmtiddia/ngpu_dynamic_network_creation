# Cortical microcircuit model for NEST GPU

Taken from https://github.com/nest/nest-gpu/tree/main/python/Potjans_2014
<br>
Time of writing: 11.03.2023, last update to model: 13.02.2023

## Contents

### Original files

These files did not change with respect to the source at time of writing:
 - run_microcircuit.py
 - helpers.py
 - sim_params.py
 - network_params.py
 - stimulus_params.py


### Modified files

These files were modified for benchmarking purposes:
 - network.py:
   - Added get_network_size function to get total number of neurons. (l200)
   - Disabled Prepare and Cleanup call from connect function (l97): To properly measure calibration time, Prepare and Cleanup functions were commented.

### Additional files

These files were added for benchmarking purposes:
 - run_benchmark.py: Python script based on the original simulation script of the model with additional adaptations for benchmarking, notably the addition of command line argument handling, simulation timers (cf Models sub-section in #INSERT PAPER REF#), and data exporting to json files.
  - Added handling of different Nested Loop algorithms passed as argument.
 - gather_data.py: Python script designed to collect the data from all of the simulation runs of a benchmark and compute the mean values and the standard deviation of the simulation timers.
 - benchmark.sh: Bash script to automatically benchmark the model with 10 different random generation seeds and collect the data.
 