#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Gather data script for NEST GPU.
# Collects all the JSON data generated by each individual simulation in a given directory.
# Used by benchmark.sh after all the simulation runs.
# execute with:
#	python3 gather_data.py PATH [--out=FILE]
#		with PATH the path to the top directory containing the results of multiple simulations
#		with FILE an optional argument to the path for the output file.
#			defaults to "data.json"

import json
import numpy as np

from pathlib import Path
from argparse import ArgumentParser


def get_paths():
    """
    Parses argument given in command line when launching script.

    Required:
     - path (string): the path to the top directory containing the results of multiple simulations

    Optional:
     - --out (string): optional argument to the path for the output file. Defaults to "data.json".

    Returns:
     - Tuple of path (Path) and output file (Path)
    """
    parser = ArgumentParser()
    parser.add_argument("path", type=str)
    parser.add_argument("--out", type=str, default="data.json")
    args = parser.parse_args()
    p = Path(args.path)
    o = Path(args.out)
    assert p.is_dir() and (not o.exists() or o.is_file())
    if o.is_file():
        print(f"WARNING: overriding {o}")

    return p, o


def get_json_results(path: Path):
    """
    Iteratively loads the content of every JSON file found in depth=1 of given directory.
    Build a JSON-like dictionary with same structure as input JSONs,
    containing lists of all the collected values.

    Arguments:
     - path (Path): path to the top directory containing the results of multiple simulations

    Returns:
     - results (dict): all the collected data as a dictionary.
    """
    results = {}
    for p in path.glob("*/*.json"):
        with p.open() as f:
            data = json.load(f)

        d_conf = data["conf"]
        d_algo = d_conf.pop("nested_loop_algo")
        d_seed = d_conf.pop("seed")
        d_timers = data["timers"]

        if results == {}:
            results[d_algo] = {
                "conf": d_conf,
                "seeds": [],
                "timers": {}
            }
        r_algo = results[d_algo]

        # Seeds must be unique
        r_seeds = r_algo["seeds"]
        assert d_seed not in r_seeds
        r_seeds.append(d_seed)

        # Get all timers data
        r_timers = r_algo["timers"]
        if r_timers == {}:
            for timer in d_timers:
                r_timers[timer] = [d_timers[timer]]
        else:
            for timer in d_timers:
                r_timers[timer].append(d_timers[timer])

    # Sanity check
    for algo in results:
        num_seeds = len(results[algo]["seeds"])
        for timer in results[algo]["timers"]:
            assert len(results[algo]["timers"][timer]) == num_seeds

    return results


def get_statistics(results: dict):
    """
    Given a dictionary of results, for each list in the timers sub-dictionary,
    computes the mean and standard deviation and replaces the list by a sub-dictionary containing these values.
    Builds a JSON-like dictionary with same structure as input JSON-like dictionary.

    Arguments:
     - results (dict): all the collected data as a dictionary.

    Returns:
     - statistics (dict): all the computed data as a dictionary.
    """
    stats = {}
    for algo in results:
        r_algo = results[algo]

        if stats == {}:
            stats[algo] = {
                    "conf": r_algo["conf"],
                    "seeds": r_algo["seeds"],
                    "timers": {}
                }
        s_algo = stats[algo]


        r_timers = r_algo["timers"]
        s_timers = s_algo["timers"]
        for timer in r_timers:
            times = np.array(r_timers[timer]) / 1e9
            s_timers[timer] = {
                "mean": np.mean(times),
                "std": np.std(times)
            }
    
    return stats


def save_statistics(stats: dict, out: Path):
    """
    Given a JSON-like dictionary of statistics, and a path to a file,
    saves as JSON data to file.

    Arguments:
     - statistics (dict): all the computed data as a dictionary.
     - out (Path): Path object to output file.
    """
    with out.open("w") as f:
        json.dump(stats, f, indent=4)


def main():
    """
    Main function of script.
    """
    path, out = get_paths()
    res = get_json_results(path)
    stats = get_statistics(res)
    save_statistics(stats, out)


if __name__ == "__main__":
    main()
