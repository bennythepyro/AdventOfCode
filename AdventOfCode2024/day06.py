from enum import Enum
import sys
from typing import Dict, List
import myUtil

# lines = myUtil.openFile()
lines = myUtil.openFile("day06.txt")

part1 = 0
part2 = 0

#########


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

    def nextDir(direction: "Direction") -> "Direction":
        match (direction):
            case Direction.UP:
                return Direction.RIGHT
            case Direction.RIGHT:
                return Direction.DOWN
            case Direction.DOWN:
                return Direction.LEFT
            case Direction.LEFT:
                return Direction.UP


##################


class Marker(Enum):
    GUARD = 1
    # UNVISITED = 2
    VISTED = 3
    BLOCKER = 4
    VISITED_UP = 5
    VISITED_RIGHT = 6
    VISITED_DOWN = 7
    VISITED_LEFT = 8

    def visitedMarker(direction: Direction) -> "Marker":
        match (direction):
            case Direction.UP:
                return Marker.VISITED_RIGHT
            case Direction.RIGHT:
                return Marker.VISITED_DOWN
            case Direction.DOWN:
                return Marker.VISITED_LEFT
            case Direction.LEFT:
                return Marker.VISITED_UP


class MapCell:

    def __init__(self):
        self.data: Dict[Marker, bool] = dict()
        self.reset()

    def reset(self):
        for mark in Marker:
            self.data[mark] = False

    def setVisited(self, direction: Direction):
        self.data[Marker.VISTED] = True
        self.data[Marker.visitedMarker(direction)] = True

    def isVisited(self) -> bool:
        return self.data[Marker.VISTED]

    def isGuard(self) -> bool:
        return self.data[Marker.GUARD]

    def setMarker(self, marker: Marker):
        self.data[marker] = True

    def getMarker(self, marker: Marker) -> bool:
        return self.data[marker]

    def isBlocker(self) -> bool:
        return self.data[Marker.BLOCKER]


##########################################


class Map:
    # data: List[List[MapCell]] = list()

    ##############
    def __init__(self, lines: List[str]):

        self.matrix: Dict[int, Dict[int, MapCell]] = dict()
        self.direction: Direction = Direction.UP
        self.guardPos: Dict[str, int] = dict()
        self.looping: bool
        self.steps = 0

        rows = len(lines)
        cols = len(lines[0].strip())

        for row in range(rows):
            self.matrix[row] = dict()
            for col in range(cols):
                self.matrix[row][col] = MapCell()

        print(f"{len(self.matrix.keys())} x {len(self.matrix[0].keys())}")

        self.reset(lines)

    ##############

    def reset(self, lines: List[str]):

        for rowKey, rowVal in self.matrix.items():
            for colKey, cell in rowVal.items():
                # print(f"cell at {rowKey} : {colKey}")
                cell.reset()
                match lines[rowKey][colKey]:
                    case "^":
                        cell.setMarker(Marker.GUARD)
                    case "#":
                        cell.setMarker(Marker.BLOCKER)
                    case _:
                        pass

        if not self.defineStart():
            print("Error, can't fine start")
        self.looping = False
        self.steps = 0

    # def addLine(self, input: str) -> None:
    #
    #     tempList: List[Marker] = list()
    #     for index in range(len(input)):
    #         print(input[index])
    #         temp: MapCell = MapCell()
    #         match input[index]:
    #             case "^":
    #                 temp.data[Marker.GUARD] = True
    #             case "#":
    #                 temp.data[Marker.BLOCKER] = True
    #             case _:
    #                 pass
    #     self.data.append(tempList)

    def contains(self, row: int, col: int) -> bool:
        if not isinstance(row, int) or not isinstance(col, int):
            print(f"Error, row: {row} type: {type(row)} col: {col} type: {type(col)}")
        if row not in self.matrix:
            return False
        if col not in self.matrix[row]:
            return False

        return True

    def get(self, row: int, col: int) -> MapCell:
        if not isinstance(row, int) or not isinstance(col, int):
            print(f"Error, row: {row} type: {type(row)} col: {col} type: {type(col)}")
        if not self.contains(row, col):
            return " "
        # print(self.data[row][col])
        return self.matrix[row][col]

    def defineStart(self) -> bool:
        for row in self.matrix.keys():
            for col in self.matrix[row].keys():
                if self.get(row, col).isGuard():
                    self.guardPos["row"] = row
                    self.guardPos["col"] = col
                    self.direction = Direction.UP
                    return True

        return False

    rowDelta: Dict[Direction, int] = {
        Direction.UP: -1,
        Direction.DOWN: 1,
        Direction.LEFT: 0,
        Direction.RIGHT: 0,
    }
    colDelta: Dict[Direction, int] = {
        Direction.UP: 0,
        Direction.DOWN: 0,
        Direction.LEFT: -1,
        Direction.RIGHT: 1,
    }

    def step(self) -> bool:
        # move guard marking the path and if he moves off the map, return true
        self.steps += 1
        # print(self.data[self.guardPos["row"]][self.guardPos["col"]])

        if self.get(row=self.guardPos["row"], col=self.guardPos["col"]).getMarker(
            Marker.visitedMarker(self.direction)
        ):
            cell = self.get(row=self.guardPos["row"], col=self.guardPos["col"])
            # print(
            #     f'{self.guardPos["row"]}:{self.guardPos["col"]} - Looping: {self.looping} - Steps: {self.steps} - Direction: {self.direction}'
            # )
            # print(
            #     f'   - Cell: {cell.data.__str__()}'
            # )
            # we already were here going this direction, we are looping
            self.looping = True
            return True

        self.matrix[self.guardPos["row"]][self.guardPos["col"]].setVisited(
            self.direction
        )

        nextRow = self.guardPos["row"] + self.rowDelta[self.direction]
        nextCol = self.guardPos["col"] + self.colDelta[self.direction]

        if not self.contains(row=nextRow, col=nextCol):
            # guard left the map
            return True
        else:
            # move the guard
            if self.get(row=nextRow, col=nextCol).isBlocker():
                # turn right and try again
                self.direction = Direction.nextDir(self.direction)
                return self.step()
            else:
                # step to next pos
                self.guardPos["row"] = nextRow
                self.guardPos["col"] = nextCol
                return False

    def countVisited(self) -> int:
        output = 0
        for rowKey, row in self.matrix.items():
            for colKey, cell in row.items():
                if cell.isVisited():
                    output += 1
        return output


#################################

data: Map = Map(lines=lines)

while not data.step():
    pass

part1 = data.countVisited()

# loop through each location that was visited in part1 and place an obstacal
data2: Map = Map(lines)
for rowKey, row in data.matrix.items():
    for colKey, cell in row.items():
        # print(f"{rowKey}:{colKey} - {cell.isVisited()}")
        if cell.isVisited():

            data2.reset(lines)
            data2.matrix[rowKey][colKey].setMarker(Marker.BLOCKER)

            while not data2.step():
                pass

            print(f'{rowKey}:{colKey} - Looping: {data2.looping} - Steps: {data2.steps}')

            if data2.looping:
                part2 += 1

                # sys.exit()


print(f"Part 1 : {part1}")
print(f"Part 2 : {part2}")
