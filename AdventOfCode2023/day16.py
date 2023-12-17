import time
test= False
lines = open("C:\\Users\\Ben\\Workspace\\PublicShare\\AdventOfCode2023\\test.txt").readlines() if test \
    else open('C:\\Users\\Ben\\Workspace\\PublicShare\\AdventOfCode2023\\day16.txt').readlines() 



energy = [[False for x in range(0,len(lines[0].strip()))] for y in range (0,len(lines))]
North = [[ False for x in range(0,len(lines[0].strip()))] for y in range (0,len(lines))] 
South = [[ False for x in range(0,len(lines[0].strip()))] for y in range (0,len(lines))] 
East = [[ False for x in range(0,len(lines[0].strip()))] for y in range (0,len(lines))] 
West = [[ False for x in range(0,len(lines[0].strip()))] for y in range (0,len(lines))] 
# direction of energy entering a cell

def reset():
    for row in range (0,len(lines)):
        for col in range(0,len(lines[0].strip())):
            energy[row][col]=0
            North[row][col]=0
            South[row][col]=0
            East[row][col]=0
            West[row][col]=0

print(f'{len(energy)} x {len(energy[0])}')
grid = []
for line in lines:
    row = []
    for char in line.strip():
        row.append(char)
    # print(row)
    grid.append(row.copy())

class Directions:
    def __init__(self,row: int,col: int,direction: str):
        self.row = row
        self.col = col
        self.direction = direction

def drillDown(row: int,col: int,direction: str):
    global North, South, East, West, grid


    #TODO add a loop to keep going until a split, the use recursion
    keepLooping = True
    while keepLooping:

            
        if row not in range(0,len(grid)):
            return
        if col not in range(0,len(grid[row])):
            return
        
        # print(f'{row}:{col} => {direction} => {grid[row][col]}')
        # time.sleep(1)
        
        energy[row][col]=True

        match direction:
            case 'E':
                if East[row][col]:
                    return
                East[row][col] = True
                match grid[row][col]:
                    case '\\': # go down
                        row = row+1
                        direction='S'
                    case '/': # go up
                        row = row-1
                        direction='N'
                    case '|': # split
                        drillDown(row+1,col,'S')
                        row = row-1
                        direction='N'
                    case _: # continue east
                        col = col+1
                        direction='E'
            case 'W':
                if West[row][col]:
                    return
                West[row][col] = True
                match grid[row][col]:
                    case '/': # go down
                        row = row+1
                        direction='S'
                    case '\\': # go up
                        row = row-1
                        direction='N'
                    case '|': # split
                        drillDown(row+1,col,'S')
                        row = row-1
                        direction='N'
                    case _: # continue west
                        col = col-1
                        direction='W'

            case 'N':
                if North[row][col]:
                    return
                North[row][col] = True
                match grid[row][col]:
                    case '/': # go east
                        col = col+1
                        direction='E'
                    case '\\': # go west
                        col = col-1
                        direction='W'
                    case '-': # split
                        drillDown(row,col-1,'W')
                        col = col+1
                        direction='E'
                    case _: # continue North
                        row = row-1
                        direction='N'
            case 'S':
                if South[row][col]:
                    return
                South[row][col] = True
                match grid[row][col]:
                    case '\\': # go east
                        col = col+1
                        direction='E'
                    case '/': # go west
                        col = col-1
                        direction='W'
                    case '-': # split
                        drillDown(row,col-1,'W')
                        col = col+1
                        direction='E'
                    case _: # continue south
                        row = row+1
                        direction='S'

# print(*grid, sep='\n')
# starting at the top left heading east
drillDown(0,0,'E')
part1=0

for row in energy:
    str = ''
    for cell in row:
        if cell:
            part1+=1
    #         str = str +'#'
    #     else:
    #         str = str +'.'
    # print(str)
print(part1)

#rows first then cols
part2 = 0
for index in range (0,len(lines)):
    # west side heading east    
    drillDown(index,0,'E')
    temp = 0
    for row in energy:
        str = ''
        for cell in row:
            if cell:
                temp+=1
    part2 = max(temp,part2)
    reset()
    # east side heading west    
    drillDown(index,len(lines[0])-1,'W')
    temp = 0
    for row in energy:
        str = ''
        for cell in row:
            if cell:
                temp+=1
    part2 = max(temp,part2)
    reset()
#now cols
for index in range (0,len(lines[0])):
    # north side heading south    
    drillDown(0,index,'S')
    temp = 0
    for row in energy:
        str = ''
        for cell in row:
            if cell:
                temp+=1
    part2 = max(temp,part2)
    reset()
    # south side heading north    
    drillDown(len(lines)-1,index,'N')
    temp = 0
    for row in energy:
        str = ''
        for cell in row:
            if cell:
                temp+=1
    part2 = max(temp,part2)
    reset()


print(part2)