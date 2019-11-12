import time
import psutil
import datetime
import os
import json
class SystemMonitor:
    def start_monitor(self):
        path="system_monitor/"
        f = input("file name:")

        with open(path+f, 'r') as reader:
            contents=reader.read()
        data=contents+"}"     
        json_data=json.loads(data)
        cpu_max=0
        index_cpu=0
        index_mem=0
        mem_max=0
        for i in range(len(json_data)):
            index=str(i)
            if json_data[index]['cpu_percentage']>cpu_max:
               cpu_max=json_data[index]['cpu_percentage']
               index_cpu=index
            if json_data[index]['memory_percentage']>mem_max:
               mem_max=json_data[index]['memory_percentage']
               index_mem=index             
        print("cpu max",cpu_max)
        print("cpu max index",index_cpu)
        print("memory max",mem_max)
        print("memory max index",index_mem)
        print("total number of stats",len(json_data))

if __name__ == "__main__":
    monitor = SystemMonitor()
    monitor.start_monitor()
