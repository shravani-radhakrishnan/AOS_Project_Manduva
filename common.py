from concurrent.futures import process
import random

# Generates random number for waiting time and burst time
# response is obj
def RandomNumberGenerator(n):
    process_Num = []
    waiting_Time = []
    burstTime = []
    for x in range(n):
        b = random.randrange(1, 10)
        w = random.randrange(1,10)
        process_Num.append(x)
        waiting_Time.append(w)
        burstTime.append(b)
    return {'p':process_Num,'w':waiting_Time,'b':burstTime}
        

def round(data):
    process_num = data['p']
    burst = data['b']
    return process_num,burst

def prio(data):
    finalData = []
    process_num = data['p']
    burst = data['b']
    wait = data['w']
    for x in range (len(process_num)):
        subArray = []
        subArray.append(process_num[x])
        subArray.append(burst[x])
        subArray.append(wait[x])
        finalData.append(subArray)
    return finalData
