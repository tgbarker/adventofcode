#!/usr/bin/python3
import sys
import re
import string
import collections

class BagColor:
    # containedin = set()
    # contains = set()
    def __init__(self, color):
        self.color = color
        self.contains = list()
        self.containedin = set()

colorsMap = dict()

def processLine(line) : 
    matched = re.findall('(\d)? ?(\w+ *\w+)? bag+', line)
    parentColor = None
    for pos in range(0, len(matched)) :
        colorStr = matched[pos][1]
        nbBags = matched[pos][0]
        #print(matched)
        if colorStr not in colorsMap :
            colorsMap[colorStr] = BagColor(colorStr)
        if(pos == 0) : # parent color
            parentColor = colorsMap[colorStr]    
        else : # child color
            #print("Adding ", colorStr, " contained in ", parentColor.color)
            if len(nbBags) > 0 : # can have 'no other' or something else non conform
                colorsMap[parentColor.color].contains.append((int(nbBags), colorStr))
                colorsMap[colorStr].containedin.add(parentColor.color)
    #print("Parent color ", parentColor.color, "contains : ", parentColor.contains)

hasColors = set()
def checkColor(color) :
    for c in colorsMap[color].containedin :
        hasColors.add(c)
        checkColor(c)


def costColor(color) :
    count = 0
    for nbBags, c in colorsMap[color].contains :
        count += nbBags
        count += nbBags * costColor(c)
    return count

with open(sys.argv[1]) as f:
    for line in f :         
        processLine(line)

### Part 1    
checkColor('shiny gold')
print("Pt 1 : ", len(hasColors))

### Part 2
print("Pt 2 : ", costColor('shiny gold'))