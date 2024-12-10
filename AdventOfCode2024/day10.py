from enum import Enum
import math
import sys
from typing import Dict, List, Set
import myUtil

# lines = myUtil.openFile()
lines = myUtil.openFile("day10.txt")

part1 = 0
part2 = 0

#########


class Matrix:

    def __init__(self):
        self.data: Dict[str, int] = dict()
        self.rows = -1
        self.cols = -1

    def makeKey(row: int, col: int) -> str:
        return f"{row} {col}"

    def addPoint(self, row: int, col: int, value: int):
        self.rows = max(self.rows, row + 1)
        self.cols = max(self.cols, col + 1)
        self.data[Matrix.makeKey(row=row, col=col)] = value

    def getPoint(self, row: int, col: int) -> int:
        return self.data[Matrix.makeKey(row=row, col=col)]


#########

map = Matrix()
matches: Dict[str, Set[str]] = dict()
row = 0

for line in lines:
    col = 0
    for char in line.strip():
        map.addPoint(row, col, int(char))
        col += 1
    row += 1

for row in range(map.rows):
    printStr = ""
    for col in range(map.cols):
        printStr = f"{printStr}{map.getPoint(row,col)}"
    print(printStr)


#######################
def recursive1(startingKey: str, row: int, col: int):
    global part2

    thisValue = map.getPoint(row, col)
    # check for peak
    if thisValue == 9:
        matches[startingKey].add(Matrix.makeKey(row, col))
        part2 += 1
        return
    # up
    if row > 0:
        if map.getPoint(row - 1, col) == thisValue + 1:
            recursive1(startingKey=startingKey, row=row - 1, col=col)
    # down
    if row < map.rows - 1:
        if map.getPoint(row + 1, col) == thisValue + 1:
            recursive1(startingKey=startingKey, row=row + 1, col=col)
    # left
    if col > 0:
        if map.getPoint(row, col - 1) == thisValue + 1:
            recursive1(startingKey=startingKey, row=row, col=col - 1)
    # right
    if col < map.cols - 1:
        if map.getPoint(row, col + 1) == thisValue + 1:
            recursive1(startingKey=startingKey, row=row, col=col + 1)


#######################
for row in range(map.rows):
    for col in range(map.cols):
        if map.getPoint(row, col) == 0:
            key = Matrix.makeKey(row, col)
            matches[key] = set()
            recursive1(key, row, col)

# add up unique matches
for key, matchSet in matches.items():
    part1 += len(matchSet)


print(f"Part 1 : {part1}")
print(f"Part 2 : {part2}")
