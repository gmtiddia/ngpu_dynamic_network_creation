# Data

This directory contains the data generated for:
<br>
<br>
Golosio, B.; Villamar, J.; Tiddia, G.; Pastorelli, E.; Stapmanns, J.; Fanti, V.; Paolucci, P.S.; Morrison, A.; Senk, J. Runtime Construction of Large-Scale Spiking Neuronal Network Models on GPU Devices. Appl. Sci. 2023, 13, 9598. https://doi.org/10.3390/app13179598
<br>
<br>
To generate new data, check the model directories available in this repo, for more information: [README](../README.md).

## Contents

The available directories are named after the simulator used to generate the data and the platform where it was simulated, e.g.
 - [genn_20280](genn_20280): GeNN simulator using RTX 2080Ti from "Workstation 1" described in "Hardware and Software" subsection 2.5.
 - [nest_jureca](nest_jureca): NEST simulator using 1 node of the JURECA-DC cluster described in "Hardware and Software" subsection 2.5.
 - [nestgpu_jusuf](nestgpu_jusuf): NEST GPU simulator using 1 node equipped with a V100 GPU of the JUSUF cluster described in "Hardware and Software" subsection 2.5.

<br>

Depending on the simulator, a single or multiple data sets can be found, the directory hierarchy will be described in the next sections.
<br>
For each benchmarked model, the data from each seed was kept along the standard output stream and standard error stream of the execution.
<br>
The "gathered" data is found at the top of each benchmark data directory and named as ```benchmark_data_SIMULATION_ID.json``` with the simulation ID composed of the date and time of running the benchmark.

### Cortical Microcircuit Data

GeNN directories contain a single set of microcircuit benchmarking data.
<br>
NEST and NEST GPU directories contain data sets for microcircuit benchmarks using DC inputs or poisson generators, these are stored in ```dc_input_benchmark``` and ```poi_gen_benchmark``` directories respectively.
<br>
NEST GPU directories contain benchmarking sets for both the "offboard" version and "onboard" version described in [README](../README.md). To distinguish them, ```offboard``` and ```onboard``` prefixes were added to the corresponding directories.

### Two population network with Izhikevich neurons

This network was only implemented with NEST GPU "onboard" version and benchmark were only done in the JURECA-DC cluster.
Data files can be found in [onboard_benchmark](nestgpu_jureca/two_population_benchmarks/onboard_benchmark/)
