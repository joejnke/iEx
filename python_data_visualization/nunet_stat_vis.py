import argparse
import pandas as pd
import matplotlib.pyplot as plt


def stat_vis():
    cmd_in_parser = argparse.ArgumentParser(description="python statistical graph visualizer for nunet.io")
    cmd_in_parser.add_argument("--f_name", required=True, help=".csv file name")
    cmd_in_parser.add_argument("--plot", default="all",
                               choices=['mem_usage', 'cpu_usage', 'hdd_usage', 'network_usage', 'all'],
                               help="stat to plot")  # choice=first row of the csv file, if available

    cmd_args = cmd_in_parser.parse_args()
    if cmd_args.plot == "all":
        names = ['mem_usage', 'cpu_usage', 'hdd_usage', 'network_usage']
    else:
        names = cmd_args.plot

    # to be moved before the usage of plot argument
    # use plot only when ploting not when importing the csv file
    # mutiple values for plot
    nunet_stat = pd.read_csv(cmd_args.f_name, names=names)

    # use plot here
    nunet_stat.plot.line(subplots=True, layout=(4, 1), figsize=(10, 10))
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    stat_vis()
