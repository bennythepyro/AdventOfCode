test= True

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
    
