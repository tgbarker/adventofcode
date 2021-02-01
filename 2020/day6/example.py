#!/usr/bin/python3
import sys
import re
import string

def isLineEmpty(line):
    return len(line.strip()) == 0

def getYesAnswers(line):    
    return set(c for c in line if 'a' <= c <= 'z')
    
nbYesAnswersPt1 = 0
nbYesAnswersPt2 = 0

data = [line.rstrip('\n') for line in open(sys.argv[1]).read().split('\n\n')]

for line in data: 
    print("--\n",line)
    nbYesAnswersPt1 += len(getYesAnswers(line)) # pt1
    #pt2 
    allYes = set(string.ascii_lowercase)
    for person in line.split('\n') :
        allYes = allYes.intersection(getYesAnswers(person))
    nbYesAnswersPt2 += len(allYes)

print("Pt1 : " , nbYesAnswersPt1)
print("Pt2 : " , nbYesAnswersPt2)