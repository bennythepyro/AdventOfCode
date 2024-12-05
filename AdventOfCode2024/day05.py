import math
from typing import Dict, List, Set
import myUtil

# lines = myUtil.openFile()
lines = myUtil.openFile("day05.txt")

part1 = 0
part2 = 0

#########


class Rules:

    beforeDict: Dict[int, Set[int]]

    def __init__(self):
        self.beforeDict = dict()

    def addRule(self, firstNum: int, lastNum: int):
        if firstNum not in self.beforeDict.keys():
            self.beforeDict[firstNum] = set()

        self.beforeDict[firstNum].add(lastNum)

    def findInvalidIndex(self, seq: List[int]) -> int:

        for index in range(1, len(seq)):

            subset1: Set[int] = set(seq[:index])
            subset2: Set[int] = self.beforeDict.get(seq[index], set())
            # print(f"{subset1.intersection(subset2)} from {subset1} AND {subset2}")

            if len(subset1.intersection(subset2)) != 0:
                return index

        return -1

    def sequenceIsValid(self, seq: List[int]) -> bool:

        # for index in range(1, len(seq)):

        #     subset1: Set[int] = set(seq[:index])
        #     subset2: Set[int] = self.beforeDict.get(seq[index], set())
        #     # print(f"{subset1.intersection(subset2)} from {subset1} AND {subset2}")

        #     if len(subset1.intersection(subset2)) != 0:
        #         return False

        # return True
        return self.findInvalidIndex(seq) == -1

    def fixSequence(self, seq: List[int]) -> int:

        invalidFirstIndex = self.findInvalidIndex(seq)

        # find the invalid number that comes before this number
        for index in range(invalidFirstIndex) :
            if seq[index] in self.beforeDict[seq[invalidFirstIndex]]:
                # swap numbers and try again
                newSeq = seq.copy()
                newSeq[index] = seq[invalidFirstIndex]
                newSeq[invalidFirstIndex] = seq[index]
                return self.fixSequence(newSeq)

        return seq[math.floor(len(seq) / 2)]


#####
rules = Rules()
foundBlank = False

for line in lines:
    if foundBlank:
        seq = [int(x) for x in line.strip().split(",")]
        if rules.sequenceIsValid(seq):
            part1 += seq[math.floor(len(seq) / 2)]
            print(f"Adding {seq[math.floor(len(seq) / 2)]} from {seq}")
        else:
            part2 += rules.fixSequence(seq=seq)

    elif len(line.strip()) == 0:
        foundBlank = True
    else:
        temp = line.strip().split("|")
        rules.addRule(firstNum=int(temp[0]), lastNum=int(temp[1]))

# print(rules.beforeDict)


print(f"Part1 : {part1}")
print(f"Part2 : {part2}")
