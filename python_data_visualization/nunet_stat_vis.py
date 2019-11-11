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
    cmd_in_parser.add_argument("--f_name", required=True, help=".json file name")
    cmd_in_parser.add_argument("--plot", default="all",
                               choices=['cpu_percentage',
                                        'memory_percentage',
                                        'hdd_percentage',
                                        'network_percentage',
                                        'all'],
                               help="statistics data to plot")
    cmd_in_parser.add_argument("--bins", type=int, default=10, help="number of bins to use")

    cmd_args = cmd_in_parser.parse_args()
    nunet_stat = load_json(cmd_args.f_name)
    # fig, stat_subplot = plt.subplots(nunet_stat.shape[1], 1)
    # fig.suptitle("Resource usage statistics")

    # nunet_stat.groupby(pd.cut(nunet_stat['cpu_percentage'], bins=10))['cpu_percentage'].mean().plot()
    # print(nunet_stat)
    # nunet_stat['bin_avg'] = pd.cut(nunet_stat['cpu_percentage'], bins=2)
    # cpu_df = nunet_stat.groupby(['bin'])['cpu_percentage'].mean()
    # cpu_df.plot.line()
    # plt.plot(cpu_df)
    # print(cpu_df.shape[tuple((-0.0051, 2.55))])

    time_stamp = list()
    avg_cpu_perc = list()

    steps = ceil(nunet_stat.shape[0] / cmd_args.bins)
    start = 0
    nunet_stat['bin_avg_cpu'] = nunet_stat['cpu_percentage']
    for bin_end in range(steps, nunet_stat.shape[0] + steps, steps):
        time_stamp.append(bin_end - steps / 2)
        if bin_end >= nunet_stat.shape[0]:
            avg_cpu_perc.append(mean(nunet_stat['cpu_percentage'][start:nunet_stat.shape[0]]))
            nunet_stat['bin_avg_cpu'][start:nunet_stat.shape[0]] = mean(nunet_stat['cpu_percentage']
                                                                    [start:nunet_stat.shape[0]])
            # print("end: ", nunet_stat['cpu_percentage'][start:nunet_stat.shape[0]])
            # if nunet_stat['cpu_percentage'][start:nunet_stat.shape[0]].max() > 100:
            #     print("max of cpu: ", nunet_stat['cpu_percentage'][start:nunet_stat.shape[0]].max())
            #     print("index of max of cpu: ", nunet_stat['cpu_percentage'][start:nunet_stat.shape[0]].idxmax())
            break
        else:
            avg_cpu_perc.append(mean(nunet_stat['cpu_percentage'][start:bin_end]))
            nunet_stat['bin_avg_cpu'][start:nunet_stat.shape[0]] = mean(nunet_stat['cpu_percentage']
                                                                    [start:bin_end])
            # print(nunet_stat['cpu_percentage'][start:bin_end])
            # if nunet_stat['cpu_percentage'][start:bin_end].max() > 100:
            #     print("max of cpu: ", nunet_stat['cpu_percentage'][start:bin_end].max())
            #     print("index of max of cpu: ", nunet_stat['cpu_percentage'][start:bin_end].idxmax())
        start = bin_end

    print("final max of cpu: ", nunet_stat['cpu_percentage'].max())
    print("final index of max of cpu: ", nunet_stat['cpu_percentage'].idxmax())
    print("timestamp:", time_stamp)
    print("timestamp size :", len(time_stamp))
    print("avg: ", avg_cpu_perc)
    # print(nunet_stat.shape[0])
    # print(nunet_stat)
    #
    # if cmd_args.plot == "all":
    #     # plot cpu_percentage with the bin's average
    #     stat_subplot[0].plot(time_stamp, avg_cpu_perc)
    #     stat_subplot[0].set_title("CPU usage")
    #     # stat_subplot[0].xlabel("Time ")
    #     # stat_subplot[0].ylabel("Average cpu percentage")
    #
    #     # plot mem_percentage
    #     stat_subplot[1].plot(nunet_stat['memory_percentage'])
    #     stat_subplot[1].set_title("Memory usage")
    # elif cmd_args.plot == 'cpu_percentage':
    #     # plot cpu_percentage with the bin's average
    #     stat_subplot[0].plot(time_stamp, avg_cpu_perc)
    #     stat_subplot[0].set_title("CPU usage")
    #     # stat_subplot[0].xlabel("Time ")
    #     # stat_subplot[0].ylabel("Average cpu percentage")
    # else:
    #     nunet_stat[[cmd_args.plot]].plot.line()  # plot only told to plot
    #
    # plt.tight_layout()
    # plt.show()

    if cmd_args.plot == "all":
        nunet_stat = nunet_stat.drop(columns='cpu_percentage')
        nunet_stat.plot.line(subplots=True, layout=(nunet_stat.shape[1], 1), figsize=(10, 10))
    else:
        nunet_stat[[cmd_args.plot]].plot.line()  # plot only told to plot

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    stat_vis()
