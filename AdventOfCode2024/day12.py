from enum import Enum
import math
import sys
from typing import Dict, List, Set
import myUtil

# lines = myUtil.openFile()
lines = myUtil.openFile("day12.txt")

part1 = 0
part2 = 0

############


class Plot:

    def __init__(self, mark: str):
        self.mark = mark
        self.region = -1
        self.perimeter = -1


class Bounds:

    def __init__(self):
        self.minRow = sys.maxsize
        self.maxRow = -sys.maxsize
        self.minCol = sys.maxsize
        self.maxCol = -sys.maxsize

    def addPoint(self, row: int, col: int):

        self.minRow = min(self.minRow, row)
        self.maxRow = max(self.maxRow, row)
        self.minCol = min(self.minCol, col)
        self.maxCol = max(self.maxCol, col)

    def __str__(self):
        return (
            f"Rows {self.minRow} - {self.maxRow}   Cols {self.minCol} - {self.maxCol}"
        )

    def __repr__(self):
        self.__str__()


#############

map = myUtil.Matrix()
regionBounds: Dict[int, Bounds] = dict()

row = 0
for line in lines:
    col = 0
    for char in line.strip():
        map.addPoint(row=row, col=col, value=Plot(char))
        col += 1
    row += 1


def getPlot(row: int, col: int) -> Plot:
    global map
    if map.contains(row, col):
        temp = map.getPoint(row, col)
        if isinstance(temp, Plot):
            return temp
    return None


# assign region
def recursive(
    map: myUtil.Matrix, row: int, col: int, matchMark: str, regionNumber: int
):
    thisPlot = getPlot(row, col)
    if thisPlot.region != -1:
        return
    if thisPlot.mark != matchMark:
        return
    thisPlot.region = regionNumber
    regionBounds[regionNumber].addPoint(row, col)

    if map.contains(row + 1, col):
        recursive(map, row + 1, col, matchMark, regionNumber)
    if map.contains(row - 1, col):
        recursive(map, row - 1, col, matchMark, regionNumber)
    if map.contains(row, col + 1):
        recursive(map, row, col + 1, matchMark, regionNumber)
    if map.contains(row, col - 1):
        recursive(map, row, col - 1, matchMark, regionNumber)


regionNumber = 0

for row in range(map.rows):
    for col in range(map.cols):
        thisPlot = getPlot(row, col)
        if thisPlot.region == -1:
            regionBounds[regionNumber] = Bounds()
            recursive(map, row, col, thisPlot.mark, regionNumber)
            regionNumber += 1


print(f"Regions {regionNumber}")
# calc perimeter
for row in range(map.rows):
    for col in range(map.cols):
        thisPlot = getPlot(row, col)
        thisPlot.perimeter = 4

        def isSameRegion(plotA: Plot, plotB: Plot) -> bool:
            if plotA == None or plotB == None:
                return False
            return plotA.region == plotB.region

        if isSameRegion(thisPlot, getPlot(row - 1, col)):
            thisPlot.perimeter += -1
        if isSameRegion(thisPlot, getPlot(row + 1, col)):
            thisPlot.perimeter += -1
        if isSameRegion(thisPlot, getPlot(row, col + 1)):
            thisPlot.perimeter += -1
        if isSameRegion(thisPlot, getPlot(row, col - 1)):
            thisPlot.perimeter += -1

# add up area and total perimeter
for thisRegion in range(regionNumber):
    area = 0
    perimeter = 0
    thisMark = ""
    for row in range(
        regionBounds[thisRegion].minRow, regionBounds[thisRegion].maxRow + 1
    ):
        for col in range(
            regionBounds[thisRegion].minCol, regionBounds[thisRegion].maxCol + 1
        ):
            thisPlot = getPlot(row, col)
            if thisPlot.region == thisRegion:
                area += 1
                perimeter += thisPlot.perimeter
                thisMark = thisPlot.mark
    part1 += area * perimeter

    # top wall searches
    topWalls = 0
    bottomWalls = 0
    leftWalls = 0
    rightWalls = 0
    for row in range(
        regionBounds[thisRegion].minRow, regionBounds[thisRegion].maxRow + 1
    ):
        isWall = False
        for col in range(
            regionBounds[thisRegion].minCol, regionBounds[thisRegion].maxCol + 1
        ):
            if isWall:
                if getPlot(row, col).region != thisRegion or isSameRegion(
                    getPlot(row, col), getPlot(row - 1, col)
                ):
                    isWall = False
            else:
                if getPlot(row, col).region == thisRegion and not isSameRegion(
                    getPlot(row, col), getPlot(row - 1, col)
                ):
                    isWall = True
                    topWalls += 1

    isWall = False
    for row in range(
        regionBounds[thisRegion].minRow, regionBounds[thisRegion].maxRow + 1
    ):
        isWall = False
        for col in range(
            regionBounds[thisRegion].minCol, regionBounds[thisRegion].maxCol + 1
        ):
            if isWall:
                if getPlot(row, col).region != thisRegion or isSameRegion(
                    getPlot(row, col), getPlot(row + 1, col)
                ):
                    isWall = False
            else:
                if getPlot(row, col).region == thisRegion and not isSameRegion(
                    getPlot(row, col), getPlot(row + 1, col)
                ):
                    isWall = True
                    bottomWalls += 1

    isWall = False
    for col in range(
        regionBounds[thisRegion].minCol, regionBounds[thisRegion].maxCol + 1
    ):
        isWall = False
        for row in range(
            regionBounds[thisRegion].minRow, regionBounds[thisRegion].maxRow + 1
        ):
            if isWall:
                if getPlot(row, col).region != thisRegion or isSameRegion(
                    getPlot(row, col), getPlot(row, col - 1)
                ):
                    isWall = False
            else:
                if getPlot(row, col).region == thisRegion and not isSameRegion(
                    getPlot(row, col), getPlot(row, col - 1)
                ):
                    isWall = True
                    leftWalls += 1

    for col in range(
        regionBounds[thisRegion].minCol, regionBounds[thisRegion].maxCol + 1
    ):
        isWall = False
        for row in range(
            regionBounds[thisRegion].minRow, regionBounds[thisRegion].maxRow + 1
        ):
            if isWall:
                if getPlot(row, col).region != thisRegion or isSameRegion(
                    getPlot(row, col), getPlot(row, col + 1)
                ):
                    isWall = False
            else:
                if getPlot(row, col).region == thisRegion and not isSameRegion(
                    getPlot(row, col), getPlot(row, col + 1)
                ):
                    isWall = True
                    rightWalls += 1

    part2 += area * (topWalls + bottomWalls + leftWalls + rightWalls)

    # print(f"Region {thisMark} Bounds {regionBounds[thisRegion]}")
    print(
        f"Region {thisMark} Area {area} Perimeter {perimeter} Part 1 {area*perimeter} Top {topWalls} Bottom {bottomWalls} Left {leftWalls} Right {rightWalls} Walls {topWalls + bottomWalls + leftWalls + rightWalls} Part 2 {area * (topWalls + bottomWalls + leftWalls + rightWalls)}"
    )


############

print(f"Part1 : {part1}")
print(f"Part2 : {part2}")
