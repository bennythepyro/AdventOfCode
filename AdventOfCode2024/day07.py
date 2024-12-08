from enum import Enum
import sys
from typing import Dict, List
import myUtil

# lines = myUtil.openFile()
lines = myUtil.openFile("day07.txt")

part1 = 0
part2 = 0

#########


def hasMatch(index: int, goal: int, total: int, nums: List[int]) -> bool:
    if index == len(nums):
        return total == goal

    if hasMatch(index=index + 1, goal=goal, total=total + nums[index], nums=nums):
        return True

    if hasMatch(index=index + 1, goal=goal, total=total * nums[index], nums=nums):
        return True

    return hasMatch(
        index=index + 1, goal=goal, total=int(str(total) + str(nums[index])), nums=nums
    )


for line in lines:
    strs = line.strip().replace(":", "").split()
    thisList: List[int] = list()
    goal = int(strs[0])
    for numStr in strs[1:]:
        thisList.append(int(numStr))

    if hasMatch(index=1, goal=goal, total=thisList[0], nums=thisList):
        part1 += goal


print(f"Part 1 : {part1}")
