#!/usr/bin/python3
import sys
import re
import string
import collections    

def checkValues(checkNumber, listNumbers) :
    valuesToCheck = set(listNumbers)
    for comparisonNumber in listNumbers :
        if checkNumber - comparisonNumber in valuesToCheck :
            return False

    return True

fileLines = [int(line.strip()) for line in open(sys.argv[1], 'r')]

offset = 25
weaknessValue = 0

#### PT 1
for i in range(offset, len(fileLines)) :
    if checkValues(fileLines[i], fileLines[i-offset:i]) :
        weaknessValue =  fileLines[i]
        print("Pt 1 -> ", weaknessValue)
        break
    #pass
    #print(lines_list[i])

#### PT 2 
fileIndex = 0
while fileIndex < len(fileLines) :
    idx = fileIndex
    sectionSum = 0
    while sectionSum != weaknessValue and sectionSum < weaknessValue :
        sectionSum += fileLines[idx]
        idx+=1
        #print("Section sum",sectionSum)
    if sectionSum == weaknessValue :
        #print ("Pt 2 : Indexes of correct value ", fileLines[idx], fileIndex, idx)
        sectionList = fileLines[fileIndex:idx] # get list and sort for getting smallest and largest
        sectionList.sort()
        #print("Sum check : ", sum(sectionList), sectionList)
        print ("Pt 2 -> " , sectionList[0] + sectionList[len(sectionList)-1])
        break
    fileIndex +=1