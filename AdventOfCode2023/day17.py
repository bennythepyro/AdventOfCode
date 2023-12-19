import time
test= True
lines = open("C:\\Users\\Ben\\Workspace\\PublicShare\\AdventOfCode2023\\test.txt").readlines() if test \
    else open('C:\\Users\\Ben\\Workspace\\PublicShare\\AdventOfCode2023\\day17.txt').readlines() 

import sys
# sys.setrecursionlimit(8000)

grid = [[0 for x in range(0,len(lines[0].strip()))] for y in range (0,len(lines))]
effectiveHeatMap = [[140*140*10 for x in range(0,len(lines[0].strip()))] for y in range (0,len(lines))]
heatLossMap = [[140*140*10 for x in range(0,len(lines[0].strip()))] for y in range (0,len(lines))]
pathMap = [[list() for x in range(0,len(lines[0].strip()))] for y in range (0,len(lines))]

def getHeatLost(row:int,col:int):
    if row not in range(0,len(heatLossMap)):
        if col not in range(0,len(heatLossMap[row])):
            return 140*140*10
    return heatLossMap[row][col]

def setHeatLost(row:int,col:int,heatLost:int):
    # print(f'Setting heat lost at {row}:{col} = {heatLost}')
    heatLossMap[row][col]=heatLost

for y in range(0,len(lines)):
    for x in range(0,len(lines[0].strip())):
        grid[y][x] = int(lines[y][x])
# print(*grid,sep="\n")
        
# directionCount = {'N':0,'S':0,'E':0,'W':0}

part1 = 140*140*10 # max value
part2 =140*140*10
cellCount =0
path = []

# def drillDown(row:int,col:int,direction:str,directionCount:int,heatLost:int):
#     global part1
#     global cellCount
#     global path
    
#     if heatLost >= part1:
#         return
#     if row not in range(0, len(grid)):
#         return
#     if col not in range(0, len(grid[row])):
#         return
#     cellCount+=1
#     if cellCount%1000000 ==0:
#         print(path)

#     if heatLost + effectiveHeatMap[row][col] > part1:
#         return
    
#     path.append([row,col,directionCount])
#     heatLost = heatLost + grid[row][col]

#     if row == len(grid)-1 and col == len(grid[row])-1:
#         # reached the end, set the new min if valid
#         temp = part1
#         part1 = min(part1, heatLost )
#         if temp>part1:
#             print(f'New Min Found {temp} => {part1}')
#         else:
#             print(f"got to end but too big {part1}")
#         # iterate through the path to map the best way down only after a turn
#         sum = 0
#         for index in range (0,len(path)):
#             step = path[index]
#             if step[2] == 0: # first step in this direction, mark the min path
#                 effectiveHeatMap[step[0]][step[1]] = min(effectiveHeatMap[step[0]][step[1]],heatLost-sum)
#             sum += grid[step[0]][step[1]]

#     else:
#         match direction:
#             case 'N':

#                 drillDown(row, col+1, 'E', 0, heatLost)
#                 drillDown(row, col-1, 'W', 0, heatLost)
#                 if directionCount < 3:
#                     drillDown(row-1, col, 'N', directionCount+1, heatLost)
#             case 'S':
#                 drillDown(row, col+1, 'E', 0, heatLost)
#                 drillDown(row, col-1, 'W', 0, heatLost)
#                 if directionCount < 3:
#                     drillDown(row+1, col, 'S', directionCount+1, heatLost)
#             case 'E':
#                 drillDown(row+1, col, 'S', 0, heatLost)
#                 drillDown(row-1, col, 'N', 0, heatLost)
#                 if directionCount < 3:
#                     drillDown(row, col+1, 'E', directionCount+1, heatLost)
#             case 'W':
#                 drillDown(row+1, col, 'S', 0, heatLost)
#                 drillDown(row-1, col, 'N', 0, heatLost)
#                 if directionCount < 3:
#                     drillDown(row, col-1, 'W', directionCount+1, heatLost)
#     path.pop()
#     return

# drillDown(0,1,'E',0, 0)
# drillDown(1,0,'S',0, 0)
def pathHistSummary(pathIn: list):
    if len(pathIn) == 0: 
        return ['E',0]
    index = len(pathIn)-1
    dirOut = pathIn[index]
    dirCount = 1
    index += -1
    while index >=0 and dirCount < 3:
        if pathIn[index] == dirOut:
            dirCount+=1
            index+=-1
        else:
            return [dirOut,dirCount]

    # if dirCount == 3:
    #     print(f'Recent History is 3 or more {pathIn}')
    return [dirOut,dirCount]

def drillDown2(sourceRow, sourceCol, destRow, destCol, pathHist, heatLost):  
    # heatLost and pathHist are updated upon call  
    if sourceRow not in range(0, len(grid)):
        return
    if sourceCol not in range(0, len(grid[sourceRow])):
        return
    if heatLost > heatLossMap[destRow][destCol]:
        # print(f'Failed heat loss map {heatLost} >= {heatLossMap[destRow][destCol]}')
        return
    
    # time.sleep(0.5)
    # print(pathHist)

    if sourceCol == destCol and sourceRow == destRow:
        print(f'Reach the destination {sourceRow}:{sourceCol} : {destRow}:{destCol}')
        if heatLost == heatLossMap[destRow][destCol]:
            print(f'Heat map twin found {heatLost} == {heatLossMap[destRow][destCol]}')
            pathMap[destRow][destCol].append(pathHist.copy())
            return
        else:
            # found a new min heat loss
            setHeatLost(destRow,destCol,heatLost)
            pathMap[destRow][destCol] = [(pathHist.copy())]
            return
    

    # set up path
    recentPath = pathHistSummary(pathHist)
    newPath = pathHist.copy()

    EastFirst = sourceRow == destRow and sourceCol +1 == destCol
    SouthFirst = sourceRow+1 == destRow and sourceCol  == destCol
    WestFirst = sourceRow == destRow and sourceCol -1 == destCol
    NorthFirst = sourceRow-1 == destRow and sourceCol  == destCol

    if EastFirst:
        # try East
        if sourceCol + 1 < len(grid[0]) and recentPath[0] != 'W' and (recentPath[0] != 'E' or recentPath[1]<3):
            newPath.append('E')
            drillDown2(sourceRow, sourceCol+1, destRow, destCol, newPath, heatLost + grid[sourceRow][sourceCol+1])
            newPath.pop()
    elif SouthFirst:
        # try South
        if sourceRow + 1 < len(grid) and recentPath[0] != 'N' and (recentPath[0] != 'S' or recentPath[1]<3):
            newPath.append('S')
            drillDown2(sourceRow+1, sourceCol, destRow, destCol, newPath, heatLost + grid[sourceRow+1][sourceCol])
            newPath.pop()
    elif WestFirst:
        if sourceCol - 1 >=0 and recentPath[0] != 'E' and (recentPath[0] != 'W' or recentPath[1]<3):
            newPath.append('W')
            drillDown2(sourceRow, sourceCol-1, destRow, destCol, newPath, heatLost + grid[sourceRow][sourceCol-1])
            newPath.pop()
    elif NorthFirst:
        # try North
        if sourceRow - 1 >=0 and recentPath[0] != 'S' and (recentPath[0] != 'N' or recentPath[1]<3):
            newPath.append('N')
            drillDown2(sourceRow-1, sourceCol, destRow, destCol, newPath, heatLost + grid[sourceRow-1][sourceCol])
            newPath.pop()

    # try South
    if not SouthFirst and sourceRow + 1 < len(grid) and recentPath[0] != 'N' and (recentPath[0] != 'S' or recentPath[1]<3):
        newPath.append('S')
        drillDown2(sourceRow+1, sourceCol, destRow, destCol, newPath, heatLost + grid[sourceRow+1][sourceCol])
        newPath.pop()

    # try East
    if not EastFirst and sourceCol + 1 < len(grid[0]) and recentPath[0] != 'W' and (recentPath[0] != 'E' or recentPath[1]<3):
        newPath.append('E')
        drillDown2(sourceRow, sourceCol+1, destRow, destCol, newPath, heatLost + grid[sourceRow][sourceCol+1])
        newPath.pop()

    # try West
    if not WestFirst and sourceCol - 1 >=0 and recentPath[0] != 'E' and (recentPath[0] != 'W' or recentPath[1]<3):
        newPath.append('W')
        drillDown2(sourceRow, sourceCol-1, destRow, destCol, newPath, heatLost + grid[sourceRow][sourceCol-1])
        newPath.pop()

    # try North
    if not NorthFirst and sourceRow - 1 >=0 and recentPath[0] != 'S' and (recentPath[0] != 'N' or recentPath[1]<3):
        newPath.append('N')
        drillDown2(sourceRow-1, sourceCol, destRow, destCol, newPath, heatLost + grid[sourceRow-1][sourceCol])
        newPath.pop()


def drillDown3(row:int,col:int,direction:str,directionCount:int,heatLost:int):
    global part2
    global cellCount
    global path
    
    if heatLost > 108:
        return
    if row not in range(0, len(grid)):
        return
    if col not in range(0, len(grid[row])):
        return
    if heatLost >= heatLossMap[row][col]+50:
        return
    cellCount+=1

    # if cellCount%100000 ==0:
    #     print(path)
    
    heatLost = heatLost + grid[row][col]
    path.append([row,col,directionCount])

    if row == len(grid)-1 and col == len(grid[row])-1:
        # reached the end, set the new min if valid
        temp = part2
        part2 = min(part2, heatLost )
        if temp>part2:
            print(f'New Min Found {temp} => {part2}')
            # print(path)
        # else:
            # print(f"got to end but too big {part2}")

    else:
        match direction:
            case 'N':

                drillDown3(row, col+1, 'E', 0, heatLost)
                drillDown3(row, col-1, 'W', 0, heatLost)
                if directionCount < 3:
                    drillDown3(row-1, col, 'N', directionCount+1, heatLost)
            case 'S':
                drillDown3(row, col+1, 'E', 0, heatLost)
                drillDown3(row, col-1, 'W', 0, heatLost)
                if directionCount < 3:
                    drillDown3(row+1, col, 'S', directionCount+1, heatLost)
            case 'E':
                drillDown3(row+1, col, 'S', 0, heatLost)
                drillDown3(row-1, col, 'N', 0, heatLost)
                if directionCount < 3:
                    drillDown3(row, col+1, 'E', directionCount+1, heatLost)
            case 'W':
                drillDown3(row+1, col, 'S', 0, heatLost)
                drillDown3(row-1, col, 'N', 0, heatLost)
                if directionCount < 3:
                    drillDown3(row, col-1, 'W', directionCount+1, heatLost)
    path.pop()
    return


setHeatLost(0,0,0)
pathMap[0][0] = [list()]
# heatLossMap[0][0]=0
for diag in range(1,2*len(grid)+2):
    # go along the diagnal and find the path with the least heat lost
    row = diag
    col = 0
    while row >=0:
        if row in range(0,len(grid)) and col in range (0,len(grid[0])):
            # set a resonable limit to start with
            # print(f'Searching for {row}:{col}')
            setHeatLost(row,col,grid[row][col] + min(getHeatLost(row-1,col),getHeatLost(row,col-1)) + 20)
            # heatLossMap[row][col] = grid[row][col] + min(getHeatLost(row-1,col),getHeatLost(row,col-1)) + 20
            # time.sleep(0.5)
            rowA=row-1
            colA=col
            rowB=row
            colB=col-1
            keepLoopingInner = True
            while (rowA in range(0,len(grid)) and colA in range(0,len(grid[0]))) \
                or (rowB in range(0,len(grid)) and colB in range(0,len(grid[0]))):
                keepLoopingInner = False
                if rowA in range(0,len(grid)) and colA in range(0,len(grid[0])):
                    # process this cell
                    # print(f'{rowA}:{colA} => {row}:{col}')
                    # print(pathMap[rowA][colA])
                    for thisPath in pathMap[rowA][colA]:
                        drillDown2(rowA,colA,row,col,thisPath,heatLossMap[rowA][colA])
                    keepLoopingInner = True
                    rowA += -1
                    colA += 1
                if rowB in range(0,len(grid)) and colB in range(0,len(grid[0])):
                    # process this cell
                    # print(f'{rowB}:{colB} => {row}:{col}')
                    # print(pathMap[rowB][colB])
                    for thisPath in pathMap[rowB][colB]:
                        drillDown2(rowB,colB,row,col,thisPath,heatLossMap[rowB][colB])
                    keepLoopingInner = True
                    rowB += 1
                    colB += -1


        row+=-1
        col+=1


print(*heatLossMap,sep='\n')

# debug, show the path that was used
debugPath = grid.copy()
row =0
col =0
print(len(pathMap[len(pathMap)-1][len(pathMap[0])-1]))
for i in pathMap[len(pathMap)-1][len(pathMap[0])-1][0]:
    match i:
        case 'E':
            col+=1
        case 'W':
            col+=-1
        case 'S':
            row+=1
        case 'N':
            row+=-1
    debugPath[row][col] = 0

print(*debugPath,sep='\n')
part2 = heatLossMap[len(pathMap)-1][len(heatLossMap[0])-1]

cellCount =0
drillDown3(0,0,'E',0,-grid[0][0])