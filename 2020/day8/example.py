#!/usr/bin/python3
import sys
import re
import string
import collections

class Instruction :
    def __init__(self, line):
        str = line.strip().split(" ")
        self.action = str[0]
        self.number = int(str[1])       

# This opens a handle to your file, in 'r' read mode
file_handle = open(sys.argv[1], 'r')
# Read in all the lines of your file into a list of lines
lines_list = file_handle.readlines()

instructionList = [ Instruction(line) for line in lines_list ]

#### PT 1
visitedIdx = set()
idx = 0
acc = 0

while idx not in visitedIdx :
    instruction = instructionList[idx]
    # print("INSTRUCTON -> action :", instruction.action, " number : ", instruction.number)
    visitedIdx.add(idx)
    if instruction.action == "acc" :
        acc += instruction.number
        idx += 1
    elif instruction.action == "jmp" :
        idx += instruction.number
    elif instruction.action == "nop" :
        idx+=1

print ("Pt 1 -> acc:", acc, " idx:", idx, " total instructions : ", len(lines_list) )

### PT 2
def tryInstructions(instructions) :
    alreadyVisited = set()
    acc = 0
    idx = 0
    while True :
        if idx == len(instructions) :
            return acc
        elif idx in alreadyVisited :
            # print("Detected infinite loop at : ", idx)
            return None        
        
        alreadyVisited.add(idx)
        instruction = instructions[idx]
        if instruction.action == "acc" :
            acc += instruction.number
            idx += 1
        elif instruction.action == "jmp" :
            idx += instruction.number
        elif instruction.action == "nop" :
            idx+=1

for i in range(len(instructionList)) :    
    if instructionList[i].action == "jmp" : instructionList[i].action = "nop"
    elif instructionList[i].action == "nop" : instructionList[i].action = "jmp"
    res = tryInstructions(instructionList)
    if res :
         print ("Pt 2 -> acc :", res)   
    # swap back values to avoid deep copy
    if instructionList[i].action == "nop" : instructionList[i].action = "jmp"
    elif instructionList[i].action == "jmp" : instructionList[i].action = "nop"