#!/usr/bin/python3
import sys
import re

correctPasswordCountPt1 = 0
correctPasswordCountPt2 = 0

with open(sys.argv[1]) as f:
    for line in f : 
        match = re.fullmatch(r'(\d+)-(\d+) (.): (.+)', line.strip())
        low, high, char, password = match.groups()
        low = int(low)
        high = int(high)  
        count = 0      
        if(low <= password.count(char) <= high):
            #print("SUCCESS : " , line)
            correctPasswordCountPt1+=1
        if( password[low-1] == char) ^ (password[high-1] == char):
            correctPasswordCountPt2+=1

print("Part 1 : " , correctPasswordCountPt1)
print("Part 2 : " , correctPasswordCountPt2)