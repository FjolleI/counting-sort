import random
import time

def compare(list):

    start_time = time.time()
    dataDict = {}
    sortedList = []
    count = 0

    for i in range(0, len(list)):
        for j in range(0, len(list)):
            if list[i] > list[j]:
                count = count + 1
        d = {count: list[i]}
        dataDict.update(d)
        count = 0
    for i in range(0, len(list)):
        try:
            sortedList.append(dataDict[i])
            continue
        except:
            data = 0
    print("%s sec " % (time.time() - start_time))

def distribute(list):

    start_time = time.time()
    dataDict = {}
    unique = set(list)
    unique = sorted(unique)
    distributionValues = {}
    sortedList = []
    count = 0
    for i in range(0, len(list)):
        for j in range(0, len(list)):
            if list[i] == list[j]:
                count = count + 1
        encounter = {list[i]: count}
        dataDict.update(encounter)
        dataDict = dict(sorted(dataDict.items(), key=lambda item: item[0]))
        count = 0

    j = 0
    for i in unique:
        j = j + dataDict[i]
        dValues = {i: j}
        distributionValues.update(dValues)

    for i in dataDict.keys():
        for j in range(0, dataDict[i]):
            if dataDict[i] == 0:
                break
            else:
                sortedList.append(i)
                dataDict[i] = dataDict[i] - 1
                continue

    print("%s sec " % (time.time() - start_time))

dataLists =[]
for i in range(0,1000):
    number = random.randint(0,1000)
    dataLists.append(number)

print('\nComparison: \n')

compare(dataLists)
print('\nDistribution: \n')

distribute(dataLists)