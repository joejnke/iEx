import sys
import pandas as pd
import matplotlib.pyplot as plt

def stat_vis():
    names = ['mem_usage', 'cpu_usage', 'hdd_usage', 'network_usage']  # first row of the csv file, if available
    nunet_stat = pd.read_csv('sample_cpu_mem_usage.csv', names=names)
    nunet_stat.plot.line(subplots=True, layout=(4, 1), figsize=(10, 10))
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    stat_vis()
