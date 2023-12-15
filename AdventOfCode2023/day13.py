test= False
lines = open("C:\\Users\\Ben\\Workspace\\PublicShare\\AdventOfCode2023\\test.txt").readlines() if test \
    else open('C:\\Users\\Ben\\Workspace\\PublicShare\\AdventOfCode2023\\day13.txt').readlines() 

grids=[]
grid = []
for line in lines:
    if len(line.strip()) == 0:
        #start new grid
        # print(grid)
        grids.append(grid.copy())
        grid = []
    else:
        temp = []
        for i in line.strip():
            temp.append(i)
        grid.append(temp)
grids.append(grid.copy())
grid = []

canidateCols = []
canidateRows = []

def drillDownVertQuick(grid,row,col):
    if grid[row][col] == grid[row][col+1]:
        if row == len(grid) - 1: # last row, add to canidates
            canidateCols.append(col)
        else:
            drillDownVertQuick(grid,row+1,col)
        

def drillDownHorzQuick(grid,row,col):    
    if grid[row][col] == grid[row+1][col]:
        if col == len(grid[row]) - 1: # last col, add to canidates
            canidateRows.append(row)
        else:
            drillDownHorzQuick(grid,row,col+1)

def digDeepVert(grid,col: int): # candiate found, look deeper
    col1 = col
    col2 = col+1
    while col1 in range (0,len(grid[0])) and col2 in range(0,len(grid[0])):
        #look for mismatches down the column
        for row in range(0,len(grid)):
            if grid[row][col1] != grid[row][col2]:
                return -1
        
        # step cols
        col1 += -1
        col2 += 1
    print(f'Found Col at {col}')
    return col + 1 

def digDeepVert2(grid,col: int): # candiate found, look deeper
    col1 = col
    col2 = col+1
    smudgeFound = False
    while col1 in range (0,len(grid[0])) and col2 in range(0,len(grid[0])):
        #look for mismatches down the column
        for row in range(0,len(grid)):
            if grid[row][col1] != grid[row][col2]:
                if not smudgeFound:
                    smudgeFound = True
                else: #smudge already found, this is not the line
                    return -1
        
        # step cols
        col1 += -1
        col2 += 1
    if not smudgeFound:
        return -1
    print(f'Found Col at {col}')
    return col + 1 

def digDeepHorz(grid,row: int): # candiate found, look deeper
    row1 = row
    row2 = row+1
    while row1 in range (0,len(grid)) and row2 in range(0,len(grid)):
        #look for mismatches down the column
        for col in range(0,len(grid[row])):
            if grid[row1][col] != grid[row2][col]:
                return -1
        
        # step cols
        row1 += -1
        row2 += 1
    # if you get here, the answer is this one, return OG col
    print(f'Found Row at {row}')
    return row + 1 

def digDeepHorz2(grid,row: int): # candiate found, look deeper
    row1 = row
    row2 = row+1
    smudgeFound = False
    while row1 in range (0,len(grid)) and row2 in range(0,len(grid)):
        #look for mismatches down the column
        for col in range(0,len(grid[row])):
            if grid[row1][col] != grid[row2][col]:
                if not smudgeFound:
                    smudgeFound = True
                else: #smudge already found, this is not the line
                    return -1
        
        # step cols
        row1 += -1
        row2 += 1
    # if you get here, the answer is this one, return OG col
    if not smudgeFound:
        return -1
    print(f'Found Row at {row}')
    return row + 1 

part1 = 0
part2 = 0

for grid in grids:
    canidateCols = []
    canidateRows = []
    tempCol = -1
    tempRow = -1
    tempCol2 = -1
    tempRow2 = -1

    for col in range (0,len(grid[0])-1):
        tempCol = max(tempCol,digDeepVert(grid,col))
        tempCol2 = max(tempCol2,digDeepVert2(grid,col))
    
    for row in range (0,len(grid)-1):
        tempRow = max(tempRow,digDeepHorz(grid,row))
        tempRow2 = max(tempRow2,digDeepHorz2(grid,row))
   
    print(f'{tempCol} : {tempRow} : {tempCol2} : {tempRow2}') 
    part1 += 0 if tempCol == -1 else tempCol
    part1 += 0 if tempRow == -1 else tempRow*100
    part2 += 0 if tempCol2 == -1 else tempCol2
    part2 += 0 if tempRow2 == -1 else tempRow2*100

print(part1)
print(part2)