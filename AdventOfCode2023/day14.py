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

def keepSliding(row: int,col: int,slideLength):
    global platform
    if row-slideLength not in range(0,len(platform)):
        return False
    if col not in range(0,len(platform[row])):
        return False
    if platform[row-slideLength][col] == '.':
        return True
    return False

part1 = 0

print(f'{len(platform)} x {len(platform[0])}')
for row in range (0,len(platform)):
    for col in range (0,len(platform[row])):
        if platform[row][col] == 'O': 
            # print('Found Rock')
            slide = True
            slideLength = 0
            while keepSliding(row, col, slideLength+1):
                slideLength+=1
                # print('Sliding Rock')

            # if slideLength > 0:
                # print(f'Rock slide by {slideLength}')
            platform[row][col] = '.'
            platform[row-slideLength][col] = 'O'
            # print(f'{row}x{col} Adding {len(platform)-(row-slideLength)} slide by {slideLength}')
            part1 += len(platform)-(row-slideLength)
print(part1)
# print(*platform, sep='\n')