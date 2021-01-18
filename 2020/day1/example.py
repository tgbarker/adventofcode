#!/usr/bin/python3
import sys

diffMap = dict()
year : int = 2020
   
def read_ints(file) -> [int]:
    file = open(file, "r")

    lines = file.read().splitlines()
    ints = []

    for i in range(len(lines) - 1):
        ints.append(int(lines[i]))

    file.close()
    return ints

numbs = read_ints(sys.argv[1])

#
# PART 1
#
for line in numbs:
    if(line in diffMap) :        
        print ("Part 1 : ", line * diffMap.get(line))
    else :
        diffMap[year - line] = line

#
# PART 2
#
n = len(numbs)
for i in range(n):
    for j in range(i+1, n):        
        for k in range(j+1, n):
            if numbs[i] + numbs[j] + numbs[k] == year:
                print("Part 2 : ", numbs[i]*numbs[j]*numbs[k])