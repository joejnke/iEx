import argparse
import pandas as pd
import matplotlib.pyplot as plt


def load_json(f_name):
    with open(f_name, 'r') as f:
        contents = f.read()
    data = contents + "}"

    return pd.read_json(data, orient='index')


def stat_vis():
    cmd_in_parser = argparse.ArgumentParser(description="python statistical graph visualizer for nunet.io")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    cmd_in_parser.add_argument("--f_name", required=True, help=".json file name")
    cmd_in_parser.add_argument("--plot", default="all",
                               choices=['cpu_percentage',
                                        'memory_percentage',
                                        'hdd_percentage',
                                        'network_percentage',
                                        'all'],
                               help="statistics data to plot")

    cmd_args = cmd_in_parser.parse_args()
    nunet_stat = load_json(cmd_args.f_name)

    if cmd_args.plot == "all":
        nunet_stat.plot.line(subplots=True, layout=(2, 1), figsize=(10, 10))
    else:
        nunet_stat[[cmd_args.plot]].plot.line()  # plot only told to plot

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    stat_vis()
