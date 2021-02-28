#!/usr/bin/python3
import sys
from copy import deepcopy
from collections import Counter 
import itertools 

emptySeat = "L"
occupiedSeat = "#"
floorSeat = "."
adjacents = [(-1, 0),(1, 0),(0, -1),(0, 1),(-1, -1),(-1, 1),(1, -1), (1, 1),]
oldSeatPlan = [list(line.rstrip()) for line in open(sys.argv[1])]

maxCol = len(oldSeatPlan[0])
maxRow = len(oldSeatPlan)

def countAdjacentOccupied(seats, row, col) -> int :
    occCount = 0
    for (xi, yi) in adjacents :
        xcoord = col+xi
        ycoord = row+yi
        if seatIsInBounds(seats,xcoord, ycoord) :
            if seats[ycoord][xcoord] == occupiedSeat :
                occCount+=1
        else :
            continue
    return occCount

def seatIsInBounds(seats, col, row) -> bool :
     return 0 <= col < maxCol and 0 <= row < maxRow

def processMatrix(oldSeatPlan) :
    newSeatPlan = deepcopy(oldSeatPlan)
    for row in range(len(oldSeatPlan)) :
        for col in range(len(oldSeatPlan[row])) :
            if oldSeatPlan[row][col] == floorSeat:
                continue
            occupiedAdjacentSeatCount = countAdjacentOccupied(oldSeatPlan, row, col)
            if oldSeatPlan[row][col] == emptySeat and occupiedAdjacentSeatCount == 0 :
                newSeatPlan[row][col] = occupiedSeat
            if oldSeatPlan[row][col] == occupiedSeat and occupiedAdjacentSeatCount >= 4 :
                newSeatPlan[row][col] = emptySeat
    return newSeatPlan

def countLineOfSightOccupied(seats, row, col) -> int : 
    occCount = 0
    for (xi, yi) in adjacents :
        xcoord = col+xi
        ycoord = row+yi
        if not seatIsInBounds(seats, xcoord, ycoord) :
            continue
        if seats[ycoord][xcoord] == floorSeat :
            while seatIsInBounds(seats, xcoord, ycoord) :
                xcoord = xcoord+xi
                ycoord = ycoord+yi
                if seatIsInBounds(seats, xcoord, ycoord):
                    if seats[ycoord][xcoord] == occupiedSeat :
                        occCount+=1
                        break
                    elif seats[ycoord][xcoord] == emptySeat :
                        break 
        else : 
            if seats[ycoord][xcoord] == occupiedSeat :
                occCount+=1
                continue
            elif seats[ycoord][xcoord] == emptySeat :
                continue 
    return occCount

def processMatrixPart2(oldSeatPlan) :
    newSeatPlan = deepcopy(oldSeatPlan)
    for row in range(len(oldSeatPlan)) :
        for col in range(len(oldSeatPlan[row])) :
            if oldSeatPlan[row][col] == floorSeat:
                continue
            occupiedAdjacentSeatCount = countLineOfSightOccupied(oldSeatPlan, row, col)
            if oldSeatPlan[row][col] == emptySeat and occupiedAdjacentSeatCount == 0 :
                newSeatPlan[row][col] = occupiedSeat
            if oldSeatPlan[row][col] == occupiedSeat and occupiedAdjacentSeatCount >= 5 :
                newSeatPlan[row][col] = emptySeat
    return newSeatPlan

## PART 1
lastCount = 0
nbRounds = 0
while True : 
    newSeatPlan = processMatrix(oldSeatPlan)
    occCount = dict(Counter(itertools.chain(*newSeatPlan)))[occupiedSeat]
    nbRounds +=1
    if lastCount == occCount :
        print("finished", dict(Counter(itertools.chain(*newSeatPlan))) )
        break
    oldSeatPlan = newSeatPlan
    lastCount = occCount
print(nbRounds)

## PART 2
lastCount = 0
nbRounds = 0
while True : 
    newSeatPlan = processMatrixPart2(oldSeatPlan)
    occCount = dict(Counter(itertools.chain(*newSeatPlan)))[occupiedSeat]
    nbRounds +=1
    if lastCount == occCount :
        print("finished", dict(Counter(itertools.chain(*newSeatPlan))) )
        break
    oldSeatPlan = newSeatPlan
    lastCount = occCount
print(nbRounds)