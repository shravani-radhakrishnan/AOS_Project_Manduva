import psutil
from round_robin import robin_main
from priority import priority_main
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np


# cpuUsageBefore = 

def chooseSchedulerToRun(I_CPU_Util,I_Disk_Util,I_Memory_Util):
    val = input("Name the scheduler you want to run 'round_robin' or 'priority' or 'both' :")
    if val=='round_robin':
        robin_main()
    elif val=='priority':
        priority_main()
    else:
        robin_main()
        priority_main()
    calculateUsage(I_CPU_Util,I_Disk_Util,I_Memory_Util)

def calculateUsage(I_CPU_Util,I_Disk_Util,I_Memory_Util):
    print("Before usage",I_CPU_Util,I_Disk_Util,I_Memory_Util)
    final_CPU_Utilization = psutil.cpu_percent()
    final_Disk_Utilization = psutil.disk_usage('/')
    p = psutil.Process()
    final_Memory_Utilization = p.memory_full_info()
    print("After usage",final_CPU_Utilization,final_Disk_Utilization,final_Memory_Utilization)
    
    labels = ['Priority', 'Round Robin']
    men_means = [20, 35, 30, 35, 27]
    women_means = [25, 32, 34, 20, 25]
    men_std = [2, 3, 4, 1, 2]
    women_std = [3, 5, 2, 3, 3]
    width = 0.35       # the width of the bars: can also be len(x) sequence

    fig, ax = plt.subplots()

    ax.bar(labels, men_means, width, yerr=men_std, label='Men')
    ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means,
        label='Women')

    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.legend()
    plt.show()

def main():
    
    inital_CPU_Utilization = psutil.cpu_percent()
    print("cpu usage",inital_CPU_Utilization)

    initial_Disk_Utilization = psutil.disk_usage('/')
    print("Disk usage",initial_Disk_Utilization)

    p = psutil.Process()
    initial_Memory_Utilization = p.memory_full_info()
    print("Memory Usage",initial_Memory_Utilization)

    chooseSchedulerToRun(inital_CPU_Utilization,initial_Disk_Utilization,initial_Memory_Utilization)


if __name__ == "__main__": main()


