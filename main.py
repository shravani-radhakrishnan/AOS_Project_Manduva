import psutil
from round_robin import robin_main
from priority import priority_main
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
from threading import Thread
import multiprocessing as mp
import common

def chooseSchedulerToRun(I_CPU_Util,I_Disk_Util,I_Memory_Util):
    val = input("Name the scheduler you want to run 'round_robin' or 'priority' or 'both' :")
    n = input("Number of processors:")
    n = int(n)
    resp = common.RandomNumberGenerator(n)
    if val=='round_robin':
        data = common.round(resp)
        robin_main(data,n)
    elif val=='priority':
        data = common.prio(resp)
        priority_main(data,n)
    else:
        data1 = common.round(resp)
        data2 = common.prio(resp)
        # Thread(target = robin_main()).start()
        # Thread(target = priority_main()).start()
        # print("data1---->data2",data1,data2)
        process1 = mp.Process(robin_main(data1,n))
        process2 = mp.Process(priority_main(data2,n))
        process1.start()
        process2.start()
        process1.join()
        process2.join()

        calculateUsage(I_CPU_Util,I_Disk_Util,I_Memory_Util)


def calculateUsage(I_CPU_Util,I_Disk_Util,I_Memory_Util):
    # print("Before usage",I_CPU_Util,I_Disk_Util,I_Memory_Util)
    final_CPU_Utilization = psutil.cpu_times()
    final_Disk_Utilization = psutil.disk_usage('/')
    p = psutil.Process()
    final_Memory_Utilization = p.memory_full_info()
    # print("After usage for both ----> ",final_CPU_Utilization,final_Disk_Utilization,final_Memory_Utilization)

def main():
    
    inital_CPU_Utilization = psutil.cpu_times()
    initial_Disk_Utilization = psutil.disk_usage('/')
    p = psutil.Process()
    initial_Memory_Utilization = p.memory_full_info()

    chooseSchedulerToRun(inital_CPU_Utilization,initial_Disk_Utilization,initial_Memory_Utilization)



if __name__ == "__main__": main()


