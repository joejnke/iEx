"""
HOW TO RUN:
            python nunet_stat_vis.py --f_name="path/to/.json file" --bins=300 --plot="binned_avg_cpu"
            for more on usage: python nunet_stat_vis.py -h
"""

from argparse import ArgumentParser
import pandas as pd
import matplotlib.pyplot as plt
from statistics import mean
from math import ceil


def load_json(f_name):
    with open(f_name, 'r') as f:
        contents = f.read()
    data = contents + "}"

    return pd.read_json(data, orient='index')


def stat_vis():
    cmd_in_parser = ArgumentParser(description="python statistical graph visualizer for nunet.io")
    cmd_in_parser.add_argument("--f_name", type=str, required=True, help=".json file name")
    cmd_in_parser.add_argument("--plot", default="all",
                               choices=['cpu_percentage',
                                        'binned_avg_cpu',
                                        'memory_percentage',
                                        'hdd_percentage',
                                        'network_percentage',
                                        'all'],
                               help="statistics data to plot")
    cmd_in_parser.add_argument("--bins", type=int, default=300, help="number of bins to use")

    cmd_args = cmd_in_parser.parse_args()
    nunet_stat = load_json(cmd_args.f_name)

    steps = ceil(nunet_stat.shape[0] / cmd_args.bins)
    bin_start_idx = 0
    nunet_stat['binned_avg_cpu'] = nunet_stat['cpu_percentage']
    for bin_end_idx in range(steps, nunet_stat.shape[0] + steps, steps):
        if bin_end_idx >= nunet_stat.shape[0]:
            nunet_stat['binned_avg_cpu'][bin_start_idx:nunet_stat.shape[0]] = mean(nunet_stat['cpu_percentage']
                                                                                   [bin_start_idx:nunet_stat.shape[0]])
            break
        else:
            nunet_stat['binned_avg_cpu'][bin_start_idx:nunet_stat.shape[0]] = mean(nunet_stat['cpu_percentage']
                                                                                   [bin_start_idx:bin_end_idx])
        bin_start_idx = bin_end_idx

    if cmd_args.plot == "all":
        nunet_stat = nunet_stat.drop(columns='cpu_percentage')
        nunet_stat.plot.line(subplots=True, layout=(nunet_stat.shape[1], 1), figsize=(10, 10))
    else:
        nunet_stat[[cmd_args.plot]].plot.line()  # plot only told to plot

    plt.tight_layout()
    plt.savefig(cmd_args.f_name.split('.')[0] + "_stat_plot.pdf")
    # plt.show()


if __name__ == '__main__':
    stat_vis()
