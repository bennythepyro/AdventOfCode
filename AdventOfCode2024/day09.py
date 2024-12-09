from enum import Enum
import math
import sys
from typing import Dict, List, Set
import myUtil

# lines = myUtil.openFile()
lines = myUtil.openFile("day09.txt")

part1 = 0
part2 = 0

#########


class Block:

    def __init__(self, length: int, space: bool, id: int = 0):
        self.id = id
        self.length = length
        self.space = space
        pass

    def __str__(self):
        return f"ID: {self.id}  Len: {self.length}  Space: {self.space}"

    def __repr__(self):
        return f"ID: {self.id}  Len: {self.length}  Space: {self.space}"

    def checksum(self, index: int) -> int:
        return sum(range(index, index + self.length)) * self.id


bigLine = lines[0].strip()
isSpace = False
blockList: List[Block] = list()
blockList2: List[Block] = list()
id = 0

for char in bigLine:
    blockLength = int(char)
    if isSpace:
        blockList.append(Block(length=blockLength, space=True))
        blockList2.append(Block(length=blockLength, space=True))
    else:
        blockList.append(Block(length=blockLength, space=False, id=id))
        blockList2.append(Block(length=blockLength, space=False, id=id))
        id += 1

    # toggle space indicator
    isSpace = not isSpace

# for block in blockList:
#     print(block)

########
# fill blank spaces with file contents
done = False

while not done:
    done = True
    # remove spaces at the end of the list
    while blockList[len(blockList) - 1].space:
        blockList.pop(len(blockList) - 1)

    spaceIndex = 0

    for fileIndex in range(len(blockList)):
        if blockList[fileIndex].space:
            spaceIndex = fileIndex
            done = False
            break

    if not done:
        spaceBlock = blockList.pop(spaceIndex)
        endBlock = blockList.pop(len(blockList) - 1)

        if spaceBlock.length == endBlock.length:
            # same size so just insert into the spot
            blockList.insert(spaceIndex, endBlock)
        elif spaceBlock.length > endBlock.length:
            # space is larger, add another space block then end block
            blockList.insert(
                spaceIndex,
                Block(length=spaceBlock.length - endBlock.length, space=True),
            )
            blockList.insert(spaceIndex, endBlock)
        else:  # spaceBlock.length < endBlock.length
            # space is smaller, split end block and insert into space and at the end
            blockList.insert(
                spaceIndex, Block(length=spaceBlock.length, space=False, id=endBlock.id)
            )
            blockList.append(
                Block(
                    length=endBlock.length - spaceBlock.length,
                    space=False,
                    id=endBlock.id,
                )
            )

    # for block in blockList:
    #     print(f'Block: {block}')
    # sys.exit()

# calc checksum
systemIndex = 0
for block in blockList:
    # print(f'Index: {systemIndex} - Block: {block}')

    part1 += block.checksum(systemIndex)
    systemIndex += block.length


print(f"Part 1 : {part1}")

##################################
# part 2

done = False
blockList = blockList2
blockIdLimit = len(blockList)

while not done:
    done = True
    endIndex = -1

    # find the next ID to attempt to move
    for fileIndex in reversed(range(len(blockList))):
        if not blockList[fileIndex].space and blockList[fileIndex].id < blockIdLimit:
            endIndex = fileIndex
            blockIdLimit = blockList[fileIndex].id
            done = False
            break
    if endIndex != -1:
        for spaceIndex in range(endIndex):
            if (
                blockList[spaceIndex].space
                and blockList[spaceIndex].length >= blockList[endIndex].length
            ):
                # match found, swap if equal length otherwise split and then swap
                if blockList[spaceIndex].length > blockList[endIndex].length:
                    # print(f'Making new space block at {spaceIndex}')
                    # make new space block
                    newSpace = Block(
                        length=blockList[endIndex].length,
                        space=True,
                    )
                    # shorten existing space block
                    blockList[spaceIndex].length = (
                        blockList[spaceIndex].length - blockList[endIndex].length
                    )
                    # print(blockList[spaceIndex].length)
                    # inster new space block
                    blockList.insert(spaceIndex, newSpace)
                    endIndex+=1
                

                # swap space and file blocks
                fileBlock = blockList.pop(endIndex)
                spaceBlock = blockList.pop(spaceIndex)
                # print(f'Puting {fileBlock} at {spaceIndex} and {spaceBlock} and {endIndex}')
                blockList.insert(spaceIndex, fileBlock)
                blockList.insert(endIndex, spaceBlock)
                # print(blockList)
                # sys.exit()
                break


# print("#######################")
systemIndex = 0
for block in blockList:
    # print(f"Index: {systemIndex} - Block: {block}")

    if not block.space:
        part2 += block.checksum(systemIndex)
    systemIndex += block.length


print(f"Part 2 : {part2}")
