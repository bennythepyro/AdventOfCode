test = True

def drillDown(symbolsIn, symbolIndex ,groupsIn, groupIndex):
    if groupIndex == len(groupsIn):
        return 1 # all groups found, return 1
    if groupIndex > len(groupsIn) or symbolIndex >= len(symbolsIn):
        return 0 # no matches here, return
    
    groupSize = int(groupsIn[groupIndex])
    # if symbolIndex + groupSize >= len(symbolsIn):
    #     return 0 # no room for possible matches
    
    remainingStringSize = len(symbolsIn) - symbolIndex
    remainingGroupSize = 0
    for group in groupsIn[groupIndex:]:
        remainingGroupSize+=int(group)
    
    if remainingGroupSize > remainingStringSize:
        return 0 # no more possible matches

    output = 0
    for index in range (symbolIndex,len(symbolsIn)-remainingGroupSize+1):
        if symbolsIn[index:index+groupSize].count('.') == 0:
            if groupIndex == len(groupsIn)-1:
                output+=1
            else:
                # TODO account for the space between groups
                if symbolsIn[index+groupSize] != '#':
                    output += drillDown(symbolsIn, index+groupSize+1, groupsIn, groupIndex+1)
    
    return output




lines = open('AdventOfCode2023/test.txt').readlines() if test else open('AdventOfCode2023/day12.txt').readlines() 

for line in lines:
    [symbolsStr, groupsStr] = line.split(' ')
    groups = groupsStr.strip().split(',')
    print(groups)

    print(drillDown(symbolsStr,0,groups,0))


