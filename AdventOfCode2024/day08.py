from enum import Enum
import sys
from typing import Dict, List, Set
import myUtil

# lines = myUtil.openFile()
lines = myUtil.openFile("day08.txt")

part1 = 0
part2 = 0

#########


class Coordinates:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def __str__(self):
        return f"({self.row},{self.col})"

    def __repr__(self):
        return f"({self.row},{self.col})"


symbols: Dict[str, List[Coordinates]] = dict()

row = 0
for line in lines:
    col = 0
    for char in line.strip():
        if char != ".":
            if char not in symbols:
                # print("adding list")
                symbols[char] = list()
            symbols[char].append(Coordinates(row=row, col=col))
        col += 1

    row += 1

print(symbols)

rows = len(lines)
cols = len(lines[0].strip())

antinodes = set()

for symbol, symbolList in symbols.items():
    print(symbol)
    # find the antinodes for each pair
    for index1 in range(len(symbolList)):

        antinodes.add(symbolList[index1].__str__())

        for index2 in range(len(symbolList)):
            if index1 != index2:
                deltaRow = symbolList[index1].row - symbolList[index2].row
                deltaCol = symbolList[index1].col - symbolList[index2].col
                thisRow = symbolList[index1].row
                thisCol = symbolList[index1].col

                while thisRow + deltaRow in range(rows) and thisCol + deltaCol in range(
                    cols
                ):
                    thisRow = thisRow + deltaRow
                    thisCol = thisCol + deltaCol

                    temp = Coordinates(
                        row=thisRow,
                        col=thisCol,
                    )
                    # print(f"{symbolList[index1]} x {symbolList[index2]} -> {temp}")
                    antinodes.add(temp.__str__())

    # print(antinodes)
    # antinodes.clear()


##################

print(f"{rows} x {cols}")
# print(antinodes)

# testStr = ["............" for x in range(12)]

# for antinode in antinodes:
#     temp = testStr[antinode.row]
#     testStr[antinode.row] = temp[: antinode.col] + "#" + temp[antinode.col + 1 :]

# for line in testStr:
#     print(line)

print(f"Part 1 : {len(antinodes)}")

