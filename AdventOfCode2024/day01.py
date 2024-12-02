from typing import Dict, List
import myUtil

# lines = myUtil.openFile()
lines = myUtil.openFile("day01.txt")

list1: List[int] = []
list2: List[int] = []

for line in lines:
    tempDat = line.split()
    list1.append(int(tempDat[0]))
    list2.append(int(tempDat[1]))

# print(list1)
# print(list2)

list1.sort()
list2.sort()

# print(list1)
# print(list2)

part1 = 0
hist: Dict[int,int] = dict()

for index in range(len(list1)):
    part1 += abs(list1[index] - list2[index])

    # create a histogram of numbers to do part 2 on the second list
    hist[list2[index]] = hist.get(list2[index], 0) + 1

part2 = 0

for index in range(len(list1)):

    part2 += list1[index] * hist.get(list1[index],0)


print(f"Part1 : {part1}")
print(f"Part2 : {part2}")
