test= False

lines = open("C:\\Users\\Ben\\Workspace\\PublicShare\\AdventOfCode2023\\test.txt").readlines() if test \
    else open('C:\\Users\\Ben\\Workspace\\PublicShare\\AdventOfCode2023\\day19.txt').readlines() 

class Part:
    def __init__(self,xIn: int, mIn: int, aIn: int, sIn: int):
        self._dict  = {'x' : xIn, 'm' : mIn, 'a': aIn, 's': sIn}
        self.accepted = False
        self.rejected = False
        # for key in self._dict.keys():
        #     print(f'{key} => {self._dict[key]}')

class Workflow:

    def __init__(self, input:str):
        print(f'{input}')
        self.name = input[:input.index('{')]
        self.instructions = []

        for instr in input[len(self.name)+1:-1].split(','):
            if '>' in instr: # greater than
                myIndex1 = instr.index('>')
                myIndex2 = instr.index(':')
                # add instructions [quality, comparison, value, destination
                self.instructions.append([instr[:myIndex1],'GT',int(instr[myIndex1+1:myIndex2]),instr[myIndex2+1:]]) 
            elif '<' in instr: # greater than
                myIndex1 = instr.index('<')
                myIndex2 = instr.index(':')
                # add instructions [quality, comparison, value, destination
                self.instructions.append([instr[:myIndex1],'LT',int(instr[myIndex1+1:myIndex2]),instr[myIndex2+1:]]) 
            else:
                self.instructions.append(['','',0,instr]) 
        print(f'Name = {self.name} ; {self.instructions}\n')

    def processPart(self, part : Part):
        for instr in self.instructions:
            if instr[1] == 'GT':
                if part._dict[instr[0]] > instr[2]:
                    return instr[3]
            elif instr[1] == 'LT':
                if part._dict[instr[0]] < instr[2]:
                    return instr[3]
            elif  instr[1] == '':
                return instr[3]


myWorkflows = {}
myParts = []
for line in lines:
    if line[0]=='{':
        temp = line.strip()[1:-1].split(',')
        myParts.append(Part(int(temp[0][2:]),int(temp[1][2:]),int(temp[2][2:]),int(temp[3][2:])))
    elif len(line.strip())>0:
        temp = Workflow(line.strip())
        myWorkflows[temp.name] = temp

### process parts
part1 = 0
for part in myParts:
    key = 'in'
    while not part.accepted and not part.rejected:
        key = myWorkflows[key].processPart(part)
        part.rejected = key == 'R'
        part.accepted = key == 'A'
    if part.accepted:
        for val in part._dict.values():
            part1+= val

print(part1)
part2=0
def fillRangeThisPath(theList, theRange: int, theOperation: str):
    theFillValue = False
    match theOperation:
        # make everything outside of the range given false
        case 'LT':
            # print(f'LT : {len(theList[theRange-1:])} : {4000-theRange + 1}')
            theList[theRange-1:] = [theFillValue] * (4000-theRange + 1)
        case 'GT':
            # print(f'GT : {len(theList[:theRange])} : {theRange}')
            theList[:theRange] = [theFillValue] * theRange
        case '':
            return

def fillRangeMissedPath(theList, theRange: int, theOperation: str):
    theFillValue = False
    # make everything in the range false
    match theOperation:
        case 'GT':
            # print(f'GT : {len(theList[theRange:])} : {4000-theRange}')
            theList[theRange:] = [theFillValue] * (4000-theRange) 
        case 'LT':
            # print(f'LT : {len(theList[:theRange-1])} : {theRange-1}')
            theList[:theRange-1] = [theFillValue] * (theRange-1) 
        case '':
            return

def drillDown(key:str, instrList, skippedInstrs):
    global part2
    if key == 'A':
        # apply the instrList to the ranges
        # print("vvvvvvvvvvvvvvvvvvvvvvvv")
        # # print(f'Key = {key}')
        # print(*instrList,sep='\n')
        # print()
        # print(*skippedInstrs,sep='\n')
        # print("^^^^^^^^^^^^^^^^^^^^^^^^")

        ranges = { 'x' : [True for x in range(0,4000)],
                    'm' : [True for x in range(0,4000)],
                    'a' : [True for x in range(0,4000)],
                    's' : [True for x in range(0,4000)]}

        for instr in instrList:
            if instr[0] != '':
                fillRangeThisPath(ranges[instr[0]],instr[2],instr[1])

            # match instr[0]:
            #     case 'x':
            #         fillRangeThisPath(xRange,instr[2],instr[1])
            #     case 'm':
            #         fillRangeThisPath(mRange,instr[2],instr[1])
            #     case 'a':
            #         fillRangeThisPath(aRange,instr[2],instr[1])
            #     case 's':
            #         fillRangeThisPath(sRange,instr[2],instr[1])
        # print(f'X = {ranges["x"].count(True)} ; M = {ranges["m"].count(True)} ; A = {ranges["a"].count(True)} ; S = {ranges["s"].count(True)} ; ')
        # TODO fill with the missed paths
        for instr in skippedInstrs:
            if instr[0] != '':
                fillRangeMissedPath(ranges[instr[0]],instr[2],instr[1])
        # print(f'X = {ranges["x"].count(True)} ; M = {ranges["m"].count(True)} ; A = {ranges["a"].count(True)} ; S = {ranges["s"].count(True)} ; ')
        # print(f'X = {len(ranges["x"])} ; M = {len(ranges["m"])} ; A = {len(ranges["a"])} ; S = {len(ranges["s"])} ; ')
        part2 += ranges["x"].count(True)*ranges["m"].count(True)*ranges["a"].count(True)*ranges["s"].count(True)
        return
    
    if key == 'R':
        # reject is default, do nothing
        return
    newSkippedInstrs = skippedInstrs.copy()
    for instr in myWorkflows[key].instructions:
        temp = instrList.copy()
        temp.append(instr)
        drillDown(instr[3],temp,newSkippedInstrs)
        newSkippedInstrs.append(instr)


drillDown('in',[],[])
print(part2)
