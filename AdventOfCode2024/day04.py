from typing import Dict, List
import myUtil

# lines = myUtil.openFile()
lines = myUtil.openFile("day04.txt")

part1 = 0
part2 = 0

#########


class matrix:
    data: List[List[str]] = list()

    def __init__(self):
        pass

    def addLine(self, input: str) -> None:
        self.data.append(input)

    def contains(self, row: int, col: int) -> bool:
        if row not in range(len(self.data)):
            return False
        if col not in range(len(self.data[0])):
            return False

        return True

    def get(self, row: int, col: int) -> str:
        if not self.contains(row, col):
            return " "

        return self.data[row][col]

    def rows(self) -> int:
        return len(self.data)

    def cols(self) -> int:
        if self.rows() == 0:
            return 0
        return len(self.data[0])


data: matrix = matrix()

for line in lines:
    data.addLine(line.strip())

print(f"rows: {data.rows()} cols: {data.cols()}")

key = "XMAS"


def recursive(index: int, row: int, col: int, direction: int) -> int:
    if data.get(row, col) == key[index]:
        if index == 3:
            return 1
        match direction:
            case 1:
                return recursive(
                    index=index + 1, row=row - 1, col=col, direction=direction
                )
            case 2:
                return recursive(
                    index=index + 1, row=row + 1, col=col, direction=direction
                )
            case 3:
                return recursive(
                    index=index + 1, row=row, col=col - 1, direction=direction
                )
            case 4:
                return recursive(
                    index=index + 1, row=row, col=col + 1, direction=direction
                )
            case 5:
                return recursive(
                    index=index + 1, row=row - 1, col=col - 1, direction=direction
                )
            case 6:
                return recursive(
                    index=index + 1, row=row - 1, col=col + 1, direction=direction
                )
            case 7:
                return recursive(
                    index=index + 1, row=row + 1, col=col - 1, direction=direction
                )
            case 8:
                return recursive(
                    index=index + 1, row=row + 1, col=col + 1, direction=direction
                )
    return 0


def checkForXmas(row: int, col: int) -> bool:
    valids = ("MS", "SM")
    if data.get(row, col) != "A":
        return False

    str1 = data.get(row - 1, col - 1) + data.get(row + 1, col + 1)

    if str1 not in valids:
        return False

    str1 = data.get(row - 1, col + 1) + data.get(row + 1, col - 1)

    if str1 not in valids:
        return False

    return True


for row in range(data.rows()):
    for col in range(data.cols()):
        part1 += recursive(index=0, row=row, col=col, direction=1)
        part1 += recursive(index=0, row=row, col=col, direction=2)
        part1 += recursive(index=0, row=row, col=col, direction=3)
        part1 += recursive(index=0, row=row, col=col, direction=4)
        part1 += recursive(index=0, row=row, col=col, direction=5)
        part1 += recursive(index=0, row=row, col=col, direction=6)
        part1 += recursive(index=0, row=row, col=col, direction=7)
        part1 += recursive(index=0, row=row, col=col, direction=8)

        if checkForXmas(row=row, col=col):
            part2 += 1

####
print(f"Part 1 : {part1}")
print(f"Part 2 : {part2}")
