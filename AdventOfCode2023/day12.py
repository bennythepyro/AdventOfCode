test = False

indexes = []

def drillDown(symbolsIn, symbolIndex ,groupsIn, groupIndex):
    # padded inital symbolIn list with '.' makes processing easier
    # determine if the symbols from index symbolIndex to groupsIn[groupIndex] are not '.'
    # and determine if the immediate next character is not '#' or the end of the string.

    global indexes

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

    keepLooping = True
    index = symbolIndex
    while keepLooping:
    # for index in range (symbolIndex,len(symbolsIn)):

        if symbolsIn[index-1] == '#':
            keepLooping = False
        else:
            if symbolsIn[index:index+groupSize].count('.') == 0 :

                if groupIndex == len(groupsIn)-1:

                    # last in the group is found, check for more '#'
                    if symbolsIn[index+groupSize:].count('#') == 0:
                        # print(symbolsIn[index+groupSize:])
                        # no more forced numbers left, add 1
                        indexes.append(index)
                        # print(indexes)
                        indexes.pop()
                        output+=1
                else:
                    # TODO account for the space between groups
                    if symbolsIn[index+groupSize] != '#':
                        indexes.append(index)                    
                        output += drillDown(symbolsIn, index+groupSize+1, groupsIn, groupIndex+1)
                        indexes.pop()
                    # else:
                    #     print(f'Found invalid 2 at {index}')
            index+=1
            if index >=len(symbolsIn):
                keepLooping=False
    
    return output

tracker = {}

def trackerFormat(sIndex,gIndex):
    # tracker format is 'gIndex:sIndex' = combos
    return f'{sIndex}:{gIndex}'

def drillDownBetter(symbolsIn, symbolIndex ,groupsIn, gIndex):
    # starting with the first group, determine if the sIndex works for that group
    #   if it does work in that spot, add the gIndex and the sIndex to a set with a value of how many matches are possible (init = 0)
    #   add to the list and check the list before drilling down further
    global tracker

    # see if value already exist
    temp = tracker.get(trackerFormat(symbolIndex,gIndex),-1)
    if temp >=0 :
        # print(f'Found in tracker: {trackerFormat(symbolIndex,gIndex)}=>{temp}')
        return temp
    
    # error checking
    if gIndex >= len(groupsIn):
        return 0
    
    
    if symbolIndex + int(groupsIn[gIndex]) > len(symbolsIn):
        # max length is the symbolIndex + the current group size; 
        return 0
    
    
    groupSize = int(groupsIn[gIndex])
    output = 0

    keepLooping = True
    sindex = symbolIndex
    lastGroup = gIndex == len(groupsIn)-1

    while keepLooping:        

        if symbolsIn[sindex-1] == '#':
            # missed a #, no additional possibilites
            tracker[trackerFormat(sindex,gIndex)] = 0 # not sure if this is needed
            keepLooping = False

        elif symbolsIn[sindex:sindex+groupSize].count('.') == 0 :
            # match, drill down further
            
            if lastGroup:
                # at the end of the group list, check for more #'s                
                if symbolsIn[sindex+groupSize:].count('#') == 0:
                    # none found, add 1 to output
                    output+=1
                # else do nothing, we'll get to that index soon
            else: # not the last group, keep drilling down

                if symbolsIn[sindex+groupSize] != '#':
                    # next symbol is valid, keep drilling down
                    output += drillDownBetter(symbolsIn, sindex+groupSize+1, groupsIn, gIndex+1)

        sindex+=1
        
        if sindex >=len(symbolsIn):
            keepLooping = False
    
    # add results to tracker to prevent reprocessing
    tracker[trackerFormat(symbolIndex,gIndex)] = output
    # print(f'Adding to tracker: {trackerFormat(symbolIndex,gIndex)}=>{output}')
    return output


lines = open("test.txt").readlines() if test else open('day12.txt').readlines() 

part1 = 0
part2=0

for line in lines:
    [symbolsStr, groupsStr] = line.split(' ')
    groups = groupsStr.strip().split(',')
    
    tracker = {}
    
    # padded symbolsStr makes processing easier
    temp = drillDownBetter('.'+symbolsStr+'.',1,groups,0)
    # print(f'{line.strip()} => {temp}')
    part1 += temp

    tracker = {}

    part2Goup = groups.copy()+groups.copy()+groups.copy()+groups.copy()+groups.copy()
    symbolsPart2 = '?'.join([symbolsStr,symbolsStr,symbolsStr,symbolsStr,symbolsStr])
    # padded symbolsStr makes processing easier
    temp = drillDownBetter('.'+symbolsPart2+'.',1,part2Goup,0)
    # print(f'{symbolsPart2} {part2Goup} => {temp}')
    part2 += temp

print(part1)
print(part2)


