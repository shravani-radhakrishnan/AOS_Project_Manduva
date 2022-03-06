import psutil
from round_robin import robin_main
from priority import priority_main
import plotly.express as px
import matplotlib.pyplot as plts
import numpy as np
from threading import Thread
from multiprocessing import Process

import common

def chooseSchedulerToRun():
    val = input("Name the scheduler you want to run 'round_robin' or 'priority' or 'both' :")
    n = input("Number of processors:")
    n = int(n)
    resp = common.RandomNumberGenerator(n)
    if val=='round_robin':
        start_util = calculateUsage()
        data = common.round(resp)
        robin_main(data,n)
        final_util = calculateUsage()
        common.utilization_calc(start_util,final_util)
    elif val=='priority':
        data = common.prio(resp)
        start_util = calculateUsage()
        priority_main(data,n)
        final_util = calculateUsage()
        common.utilization_calc(start_util,final_util)
    else:
        data1 = common.round(resp)
        data2 = common.prio(resp)
        start_util = calculateUsage()
        process1 = Process(target=robin_main,args=(data1,n))
        process2 = Process(target=priority_main,args=(data2,n))
        process1.start()
        process2.start()
        process1.join()
        process2.join()
        final_util = calculateUsage()
        common.utilization_calc(start_util,final_util)


def calculateUsage():
    CPU_Utilization = psutil.cpu_times()
    Disk_Utilization = psutil.disk_usage('/')
    p = psutil.Process()
    Memory_Utilization = p.memory_full_info()
    return CPU_Utilization,Disk_Utilization,Memory_Utilization

def main():
    chooseSchedulerToRun()



if __name__ == "__main__": main()


