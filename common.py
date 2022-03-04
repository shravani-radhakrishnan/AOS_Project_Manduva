import random

def randomGeneratorPriority(n):
    finalArray=[]
    n = int(n)
    for x in range(n):
        out = []
        num = x
        burstTime = random.randrange(1, 10)
        waiting = random.randrange(1,10)
        out.append(num)
        out.append(burstTime)
        out.append(waiting)
        finalArray.append(out)
    return finalArray


def randomForRound(type_data,n):
    finalArray=[]
    for x in range(n):
        if type_data == 'process':
            out = x
        else:
            out = random.randrange(1,10)
        finalArray.append(out)
    return finalArray
