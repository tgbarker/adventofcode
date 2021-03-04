#!/usr/bin/python3
import sys
from copy import deepcopy
from collections import Counter 
import itertools 

emptySeat = "L"
occupiedSeat = "#"
floorSeat = "."
adjacents = [(-1, 0),(1, 0),(0, -1),(0, 1),(-1, -1),(-1, 1),(1, -1), (1, 1),]
originalSeatingPlan = [list(line.rstrip()) for line in open(sys.argv[1])]

maxCol = len(originalSeatingPlan[0])
maxRow = len(originalSeatingPlan)

def countAdjacentOccupied(seats, row, col) -> int :
    occCount = 0
    for (xi, yi) in adjacents :
        xcoord = col+xi
        ycoord = row+yi
        occCount += countOccupiedSeat(seats, xcoord, ycoord)
    return occCount

def seatIsInBounds(seats, col, row) -> bool :
     return 0 <= col < maxCol and 0 <= row < maxRow

def countOccupiedSeat(seats, xcoord, ycoord) -> int :
    if seatIsInBounds(seats,xcoord, ycoord) :
        if seats[ycoord][xcoord] == occupiedSeat :
            return 1
        elif seats[ycoord][xcoord] == emptySeat :
            return 0
    return 0

def processMatrix(seats) :
    newSeatPlan = deepcopy(seats)
    totalOccupiedSeats = 0
    for row in range(len(seats)) :
        for col in range(len(seats[row])) :
            if seats[row][col] == floorSeat:
                continue
            occupiedAdjacentSeatCount = countAdjacentOccupied(seats, row, col)
            totalOccupiedSeats += assignNewSeat(seats, newSeatPlan, row, col, occupiedAdjacentSeatCount, 4)
    return (newSeatPlan, totalOccupiedSeats)

def assignNewSeat(oldSeats, newSeats, row, col, occupiedSeatCount, adjacentMaxCount) -> int :
    if oldSeats[row][col] == emptySeat and occupiedSeatCount == 0 :
        newSeats[row][col] = occupiedSeat
        return 1
    if oldSeats[row][col] == occupiedSeat and occupiedSeatCount >= adjacentMaxCount :
        newSeats[row][col] = emptySeat
    return 0

def countLineOfSightOccupied(seats, row, col) -> int : 
    occCount = 0
    for (xi, yi) in adjacents :
        xcoord = col+xi
        ycoord = row+yi
        if not seatIsInBounds(seats, xcoord, ycoord) :
            continue
        if seats[ycoord][xcoord] == floorSeat :
            while seatIsInBounds(seats, xcoord, ycoord) and seats[ycoord][xcoord] == floorSeat:
                xcoord = xcoord+xi
                ycoord = ycoord+yi
                occCount += countOccupiedSeat(seats, xcoord, ycoord)
        else : 
            occCount += countOccupiedSeat(seats, xcoord, ycoord) 
    return occCount

def processMatrixPart2(seats) :
    newSeatPlan = deepcopy(seats)
    totalOccupiedSeats = 0
    for row in range(len(seats)) :
        for col in range(len(seats[row])) :
            if seats[row][col] == floorSeat:
                continue
            occupiedAdjacentSeatCount = countLineOfSightOccupied(seats, row, col)
            totalOccupiedSeats += assignNewSeat(seats, newSeatPlan, row, col, occupiedAdjacentSeatCount, 5)
    return (newSeatPlan, totalOccupiedSeats)

def executeLoop(processFunction) :
    lastCount = 0
    nbRounds = 0
    oldSeatPlan = deepcopy(originalSeatingPlan)
    while True : 
        (newSeatPlan, occCount ) = processFunction(oldSeatPlan)
        nbRounds +=1
        if lastCount == occCount :
            print("finished", dict(Counter(itertools.chain(*newSeatPlan))) )
            break
        oldSeatPlan = newSeatPlan
        lastCount = occCount
    print("Nb rounds : ",nbRounds)

## PART 1
print("Part 1 : ")
executeLoop(processMatrix)

## PART 2
print("Part 2 : ")
executeLoop(processMatrixPart2)