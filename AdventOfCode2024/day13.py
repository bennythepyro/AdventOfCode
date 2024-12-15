from enum import Enum
import math
import sys
from typing import Dict, List, Set
import myUtil

# lines = myUtil.openFile()
lines = myUtil.openFile("day13.txt")

part1 = 0
part2 = 0

############


class Machine:
    class Button:
        def __init__(self, x: int, y: int):
            self.x = x
            self.y = y

        def slope(self) -> float:
            return self.y / self.x

        def __str__(self):
            return f"{self.x} : {self.y}"

        def __repr__(self):
            return self.__str__()

    def __init__(self, xA: int, yA: int, xB: int, yB: int, prizeX: int, prizeY: int):
        self.buttonA = Machine.Button(x=xA, y=yA)
        self.buttonB = Machine.Button(x=xB, y=yB)
        self.prizeX = prizeX
        self.prizeY = prizeY

    def findButtonPresses(self) -> int:
        # find the slope of the buttons
        slopeA = self.buttonA.slope()
        slopeB = self.buttonB.slope()
        prizeSlope = self.prizeY / self.prizeX
        if prizeSlope > max(slopeA, slopeB) or prizeSlope < min(slopeA, slopeB):
            # print(f"not possible 1")
            return 0

        interceptA = 0.0
        interceptB = self.prizeY - self.prizeX * slopeB

        # find the intection of the two lines, one starting at 0,0 the other at the prize point
        # y = slopeA * x + interceptA = slopeB * x + interceptB -> x = interB - inter A / slopeA - slopeB
        crossX = round((interceptB - interceptA) / (slopeA - slopeB))
        crossY = round(slopeA * crossX)
        # print(f"{crossX} : {crossY}")
        # determine if cross is possible
        pressesA = round(crossX / self.buttonA.x)
        pressesB = round((self.prizeX - crossX) / self.buttonB.x)

        # push both buttons until on line with the button slope
        if (
            pressesA * self.buttonA.x + pressesB * self.buttonB.x == self.prizeX
            and pressesA * self.buttonA.y + pressesB * self.buttonB.y == self.prizeY
        ):
            # print(f"{pressesA} : {pressesB}")
            return pressesA * 3 + pressesB
        else:
            # print(f"Not Possible 2 {pressesA} : {pressesB}")
            return 0

    def __str__(self):
        return (
            f"A {self.buttonA}  B {self.buttonB}  Prize {self.prizeX} : {self.prizeY}"
        )

    def __repr__(self):
        return self.__str__()

    def bruteForce(self):
        for pressesA in range(101):
            for pressesB in range(101):
                if (
                    pressesA * self.buttonA.x + pressesB * self.buttonB.x == self.prizeX
                    and pressesA * self.buttonA.y + pressesB * self.buttonB.y
                    == self.prizeY
                ):
                    print(f"BF {pressesA} : {pressesB}")
                    return

        print(f"Brute Force Failed")


############
aVals = list()
bVals = list()
pVals = list()
machines: List[Machine] = list()
machines2: List[Machine] = list()

for line in lines:
    splitString = line.strip().split()
    if len(splitString) > 1:
        if splitString[1] == "A:":
            aVals = [int(splitString[2][2:-1]), int(splitString[3][2:])]
        elif splitString[1] == "B:":
            bVals = [int(splitString[2][2:-1]), int(splitString[3][2:])]
        elif splitString[0] == "Prize:":
            pVals = [int(splitString[1][2:-1]), int(splitString[2][2:])]
            print(aVals)
            print(bVals)
            print(pVals)
            machines.append(
                Machine(
                    xA=aVals[0],
                    yA=aVals[1],
                    xB=bVals[0],
                    yB=bVals[1],
                    prizeX=pVals[0],
                    prizeY=pVals[1],
                )
            )
            machines2.append(
                Machine(
                    xA=aVals[0],
                    yA=aVals[1],
                    xB=bVals[0],
                    yB=bVals[1],
                    prizeX=pVals[0] + 10000000000000,
                    prizeY=pVals[1] + 10000000000000,
                )
            )

for machine in machines:
    print("*****************")
    print(machine)
    part1 += machine.findButtonPresses()
    # machine.bruteForce()

for machine in machines2:
    part2 += machine.findButtonPresses()

print(f"Part1 : {part1}")
print(f"Part2 : {part2}")
