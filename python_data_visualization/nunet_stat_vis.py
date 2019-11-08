import argparse
import pandas as pd
import matplotlib.pyplot as plt
import json
from pandas.io.json import json_normalize


def load_json(f_name):
    with open(f_name, 'r') as f:
        contents = f.read()
    data = contents + "}"
    print(pd.read_json(data, orient='index'))

    return pd.read_json(data, orient='index')

    distros_dict = json.loads(data)
    # for distro in distros_dict:
    #     print(distro, distros_dict[distro]["cpu_percentage"])

    # nycphil = json_normalize(data=distros_dict)
    # print(nycphil.head(3))
    # print(pd.read_json(data, orient='index'))
    # return pd.read_json(data, orient='index')


def stat_vis():
    cmd_in_parser = argparse.ArgumentParser(description="python statistical graph visualizer for nunet.io")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    cmd_in_parser.add_argument("--f_name", required=True, help=".csv file name")
    cmd_in_parser.add_argument("--plot", default="all",
                               choices=['cpu_percentage',
                                        'memory_percentage',
                                        'hdd_percentage',
                                        'network_percentage',
                                        'all'],
                               help="statistics data to plot")

    cmd_args = cmd_in_parser.parse_args()

    stat_names = ['mem_usage', 'cpu_usage', 'hdd_usage', 'network_usage']  # TODO: use first row of the json file
    nunet_stat = load_json(cmd_args.f_name)  # pd.read_csv(cmd_args.f_name, names=stat_names)  # TODO: use read_json

    if cmd_args.plot == "all":
        # stat_names = ['mem_usage', 'cpu_usage', 'hdd_usage', 'network_usage']
        nunet_stat.plot.line(subplots=True, layout=(2, 1), figsize=(10, 10))
    else:
        # stat_names = cmd_args.plot
        nunet_stat[[cmd_args.plot]].plot.line()  # plot only told to plot

    # to be moved before the usage of plot argument
    # use plot only when ploting not when importing the csv file
    # mutiple values for plot
    # nunet_stat = pd.read_csv(cmd_args.f_name, names=stat_names)

    # use plot here
    # nunet_stat[cmd_args.plot].plot.line()  # subplots=True, layout=(1, 1), figsize=(10, 10))
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    # load_json("nunet.json")
    stat_vis()