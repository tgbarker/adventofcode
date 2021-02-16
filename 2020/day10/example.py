#!/usr/bin/python3
import sys
# Using defaultdict() 
from collections import defaultdict 
import itertools

def read_integers(filename):
    with open(filename) as f:
        return [int(x) for x in f]

adapterList = read_integers(sys.argv[1])
adapterList.append(max(adapterList)+3) # add device adapter
adapterList.sort()

diffMap = defaultdict(int)
previousVal = 0
for adapterJoltage in adapterList : 
    diff = adapterJoltage - previousVal
    diffMap[str(diff)] += 1
    previousVal = adapterJoltage

answerPart1 = diffMap['1'] * (diffMap['3'])
print("Pt 1 : " , answerPart1)

diffMap = defaultdict(int)
differences = [1,2,3]
diffMap[0] = 1
for joltage in adapterList :
    diffMap[joltage] = 0
    for joltageDiff in differences :
        if (joltage - joltageDiff) in diffMap :
            diffMap[joltage] = diffMap[joltage] + diffMap[joltage -joltageDiff]

#print(diffMap)
print("Pt 2 : ", diffMap[max(diffMap)])