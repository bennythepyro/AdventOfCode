test= False
lines = open("C:\\Users\\Ben\\Workspace\\PublicShare\\AdventOfCode2023\\test.txt").readlines() if test \
    else open('C:\\Users\\Ben\\Workspace\\PublicShare\\AdventOfCode2023\\day14.txt').readlines() 

platform = []
for line in lines:
    row = []
    for i in line.strip():
        row.append(i)
    platform.append(row.copy())
row = []
print(*platform, sep='\n')

def keepSlidingNorth(row: int,col: int,slideLength):
    global platform
    if row-slideLength not in range(0,len(platform)):
        return False
    if col not in range(0,len(platform[row])):
        return False
    if platform[row-slideLength][col] == '.':
        return True
    return False

def keepSlidingWest(row: int,col: int,slideLength):
    global platform
    if row not in range(0,len(platform)):
        return False
    if col-slideLength not in range(0,len(platform[row])):
        return False
    if platform[row][col-slideLength] == '.':
        return True
    return False

def keepSlidingSouth(row: int,col: int,slideLength):
    global platform
    if row+slideLength not in range(0,len(platform)):
        return False
    if col not in range(0,len(platform[row])):
        return False
    if platform[row+slideLength][col] == '.':
        return True
    return False

def keepSlidingEast(row: int,col: int,slideLength):
    global platform
    if row not in range(0,len(platform)):
        return False
    if col+slideLength not in range(0,len(platform[row])):
        return False
    if platform[row][col+slideLength] == '.':
        return True
    return False

part1 = 0
cycles = 1000000000
# cycles = 3

print(f'{len(platform)} x {len(platform[0])}')
for cycle in range(0,cycles):
    #North
    for row in range (0,len(platform)):
        for col in range (0,len(platform[row])):
            if platform[row][col] == 'O': 
                # print('Found Rock')
                slideLength = 0
                while keepSlidingNorth(row, col, slideLength+1):
                    slideLength+=1
                platform[row][col] = '.'
                platform[row-slideLength][col] = 'O'
                # print(f'{row}x{col} Adding {len(platform)-(row-slideLength)} slide by {slideLength}')
    #West
    for col in range (0,len(platform[0])):
        for row in range (0,len(platform)):
            if platform[row][col] == 'O': 
                # print('Found Rock')
                slideLength = 0
                while keepSlidingWest(row, col, slideLength+1):
                    slideLength+=1
                platform[row][col] = '.'
                platform[row][col-slideLength] = 'O'
                # print(f'{row}x{col} Adding {len(platform)-(row-slideLength)} slide by {slideLength}')
    #South
    for row in range (len(platform)-1,-1,-1):
        for col in range (0,len(platform[row])):
            if platform[row][col] == 'O': 
                # print('Found Rock')
                slideLength = 0
                while keepSlidingSouth(row, col, slideLength+1):
                    slideLength+=1
                platform[row][col] = '.'
                platform[row+slideLength][col] = 'O'
                # print(f'{row}x{col} Adding {len(platform)-(row-slideLength)} slide by {slideLength}')
    #East
    for col in range (len(platform[0])-1,-1,-1):
        for row in range (0,len(platform)):
            if platform[row][col] == 'O': 
                # print('Found Rock')
                slideLength = 0
                while keepSlidingEast(row, col, slideLength+1):
                    slideLength+=1
                platform[row][col] = '.'
                platform[row][col+slideLength] = 'O'
                # print(f'{row}x{col} Adding {len(platform)-(row-slideLength)} slide by {slideLength}')
    for row in range (0,len(platform)):
        for col in range (0,len(platform[row])):
            if platform[row][col] == 'O': 
                part1+= len(platform) - row
    # if cycle % 100 == 0:
    # print(*platform, sep='\n')
    print(f'{cycle} => {part1}')
    part1=0


print(part1)
# print(*platform, sep='\n')