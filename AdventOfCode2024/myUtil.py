import os
from typing import Any, Dict


def openFile(fileName: str = "") -> list[str]:

    workingDirectory = os.path.dirname(os.path.abspath(__file__))

    if fileName == "":
        return open(os.path.join(workingDirectory, "test.txt")).readlines()
    else:
        return open(os.path.join(workingDirectory, fileName)).readlines()


class Matrix:

    def __init__(self):
        self.data: Dict[str, Any] = dict()
        self.rows = -1
        self.cols = -1

    def makeKey(row: int, col: int) -> str:
        return f"{row} {col}"

    def addPoint(self, row: int, col: int, value: Any):
        self.rows = max(self.rows, row + 1)
        self.cols = max(self.cols, col + 1)
        self.data[Matrix.makeKey(row=row, col=col)] = value

    def getPoint(self, row: int, col: int) -> Any:
        return self.data[Matrix.makeKey(row=row, col=col)]

    def contains(self, row: int, col: int) -> bool:
        return Matrix.makeKey(row, col) in self.data


class Coordinates:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def __str__(self):
        return f"({self.row},{self.col})"

    def __repr__(self):
        return f"({self.row},{self.col})"
