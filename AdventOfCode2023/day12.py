test = True

def drillDown(symbolsIn, symbolIndex ,groupsIn, groupIndex):
    # padded inital symbolIn list with '.' makes processing easier
    # determine if the symbols from index symbolIndex to groupsIn[groupIndex] are not '.'
    # and determine if the immediate next character is not '#' or the end of the string.

    if groupIndex >= len(groupsIn):
        print('Error, past the end of the group List')
        return 0 # no matches here, return
    
    groupSize = int(groupsIn[groupIndex])

    if symbolIndex + groupSize > len(symbolsIn):
        # max length is the symbolIndex + the current group size; 
        return 0
    
    # print(f'symbolIndex = {symbolIndex} : groupIndex = {groupIndex}')
    
    if symbolsIn[symbolIndex-1] == '#':
        # previous symbol make invalid combo, don't continue
        print(f'Found invalid at {symbolIndex} for group {groupIndex}')
        return 0
    
    output = 0

    for index in range (symbolIndex,len(symbolsIn)):

        if symbolsIn[index:index+groupSize].count('.') == 0 and symbolsIn[index-1] != '#' :
            if groupIndex == len(groupsIn)-1:
                # last in the group is found, add 1
                output+=1
            else:
                # TODO account for the space between groups
                if symbolsIn[index+groupSize] != '#':
                    output += drillDown(symbolsIn, index+groupSize+1, groupsIn, groupIndex+1)
                # else:
                #     print(f'Found invalid 2 at {index}')
    
    return output


lines = open("test.txt").readlines() if test else open('day12.txt').readlines() 

part1 = 0

for line in lines:
    [symbolsStr, groupsStr] = line.split(' ')
    groups = groupsStr.strip().split(',')
    
    # padded symbolsStr makes processing easier
    temp = drillDown('.'+symbolsStr+'.',1,groups,0)
    print(f'{groups} => {temp}')
    part1 += temp

print(part1)


