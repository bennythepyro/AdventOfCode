from typing import Dict, List
import myUtil

# lines = myUtil.openFile()
lines = myUtil.openFile("day03.txt")

part1 = 0
part2 = 0

#########

oneLine = " "

for line in lines:
    oneLine = oneLine + line

print(oneLine)

# for char in oneLine:
#     # print(char)

def doCalcs(input:str) -> int:
    startStr = "mul("
    endStr = ")"
    output = 0
    startIndex = 0

    while startIndex >= 0:
        startIndex = input.find(startStr, startIndex + 1)
        endIndex = input.find(endStr, startIndex + len(startStr))
        # print(f"start {startIndex} stop {endIndex}")

        if startIndex >= 0 and endIndex >= 0:
            commaIndex = input.find(",", startIndex + len(startStr))
            leftStr = input[startIndex + len(startStr) : commaIndex]
            rightStr = input[commaIndex + 1 : endIndex]
            # print(f'{oneLine[startIndex + len(startStr) : endIndex]} -> {leftStr} and {rightStr}')

            if leftStr.isdigit() and rightStr.isdigit():
                output += int(leftStr) * int(rightStr)
    return output

#######
part1 = doCalcs(oneLine)
#######

# remove all substrings from don't to do
startRemoveStr = "don't()"
stopRemoveStr = "do()"

startIndex = 0
endIndex = 0
while startIndex >= 0 and endIndex >= 0:

    startIndex = oneLine.find(startRemoveStr, 0)
    endIndex = oneLine.find(stopRemoveStr, startIndex + len(startRemoveStr))

    if startIndex >= 0 and endIndex >= 0:
        oneLine = oneLine[:startIndex] + oneLine[endIndex+len(stopRemoveStr):]

print(oneLine)
part2 = doCalcs(oneLine)


#######

print(f"Part1 {part1}")
print(f"Part2 {part2}")
