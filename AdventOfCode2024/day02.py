from typing import List
import myUtil

########################################


def isSafe(levels: List[str], debug=False) -> bool:

    increasing = False
    decreasing = False
    problemFound = False
    maxDiff = 0
    noChange = -False

    for index in range(len(levels) - 1):
        diff = int(levels[index]) - int(levels[index + 1])
        maxDiff = max(abs(diff), maxDiff)
        noChange = noChange or diff == 0

        # if too large of a jump or no change mark a problem found
        problemFound = problemFound or noChange or maxDiff > 3

        # if direction has changed
        increasing = increasing or diff < 0
        decreasing = decreasing or diff > 0

    if debug:
        print(
            f"{levels} : MaxDiff = {maxDiff} : isSafe = {not problemFound and increasing is not decreasing} : inc = {increasing} : dec = {decreasing} : noChange = {noChange}"
        )

    return not problemFound and increasing is not decreasing


########################################

# lines = myUtil.openFile()
lines = myUtil.openFile("day02.txt")
lines2: List[str] = []

part1 = 0
part2 = 0

# part 1
for line in lines:

    if isSafe(line.split()):
        part1 += 1
        part2 += 1
    else:
        lines2.append(line)

# part 2
for line in lines2:
    levels = line.split()
    # skip each index and see if there is only one problem
    for skipIndex in range(len(levels)):
        if isSafe(levels[:skipIndex] + levels[skipIndex + 1 :]):
            part2 += 1
            break


print(f"Part 1 : {part1}")
print(f"Part 2 : {part2}")
