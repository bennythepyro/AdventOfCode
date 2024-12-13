from enum import Enum
import math
import sys
from typing import Dict, List, Set
import myUtil

# lines = myUtil.openFile()
lines = myUtil.openFile("day11.txt")

part1 = 0
part2 = 0

for line in lines:
    strs = line.strip().split()

print(strs)


class Stone:
    def __init__(self, number: int):
        self.number = number


stoneLinks: Dict[int, List[int]] = dict()
stoneLinks[0] = [1]
stoneCountBefore: Dict[int, int] = dict()
stoneCountAfter: Dict[int, int] = dict()


# def blink(count: int, limit: int, input: int):
#     global stoneLinks
#     global part1

#     part1 += 1
#     if count >= limit:
#         return

#     if input == 0:
#         stoneLinks[0] = [1]
#         blink(count=count + 1, limit=limit, input=1)
#         return

#     stringLength = len(str(input))
#     if stringLength % 2 == 0:
#         thisStr = str(input)
#         stoneLinks[input] = [
#             int(thisStr[: int(stringLength / 2)]),
#             int(thisStr[int(stringLength / 2) :]),
#         ]
#         blink(count=count + 1, limit=limit, input=stoneLinks[input][0])
#         blink(count=count + 1, limit=limit, input=stoneLinks[input][1])
#         return

#     # no other rules apply, multiply
#     stoneLinks[input] = [input * 2024]
#     blink(count=count + 1, limit=limit, input=input * 2024)


def addToDict(stoneLinks: Dict[int, List[int]], number: int):
    if number in stoneLinks.keys():
        return

    numberString = str(number)
    stringLength = len(numberString)

    if (stringLength % 2) == 0:
        str1 = numberString[: int(stringLength / 2)]
        str2 = numberString[int(stringLength / 2) :]
        stoneLinks[number] = [int(str1), int(str2)]
    else:
        stoneLinks[number] = [number * 2024]


for numberStr in strs:
    number = int(numberStr)
    addToDict(stoneLinks=stoneLinks, number=number)
    stoneCountBefore[number] = stoneCountBefore.get(number, 0) + 1

for blinCount in range(0,1000):
    for number, count in stoneCountBefore.items():
        # do the link calcs if needed
        addToDict(stoneLinks=stoneLinks, number=number)
        # loop through linked numbers
        for numberLinked in stoneLinks[number]:
            # add to this linked number the count of links
            stoneCountAfter[numberLinked] = stoneCountAfter.get(numberLinked, 0) + count
    stoneCountBefore = stoneCountAfter
    stoneCountAfter = dict()

# test = "123456"
# stringLength = len(test)
# print(f"{int(test[: int(stringLength / 2)])}")
# print(f"{int(test[int(stringLength / 2) :])}")

for number, count in stoneCountBefore.items():
    part1+=count
# print(sorted(stoneLinks.keys()))

# need to map the numbers before the blink to after the blink, the count of each number at each interval,

############

print(f"Part1 : {part1}")
print(f"Part2 : {part2}")
