test= False
lines = open("C:\\Users\\Ben\\Workspace\\PublicShare\\AdventOfCode2023\\test.txt").readlines() if test \
    else open('C:\\Users\\Ben\\Workspace\\PublicShare\\AdventOfCode2023\\day15.txt').readlines() 

strs = lines[0].split(',')
# strs = ['HASH']

part1 =0 
boxes = [ [] for x in range(256)]
for str in strs:
    num = 0
    removeLens = str.count('-')>0
    addLens = str.count('=')>0
        
    if removeLens:
            # remove from box num
        
        for char in str[:-1]:
            num += ord(char)
            num = (num*17) % 256
            
        index = 0
        while index < len(boxes[num]):
            # print(f'{boxes[num][index][0]} == {str[:-1]} => {boxes[num][index][0] == str[:-1]}')
            if boxes[num][index][0] == str[:-1]:
                del boxes[num][index]
            else:
                index+=1
    else: 
        # is = sign
        temp = str.split('=')
        value = int(temp[1])
        key = temp[0]

        index = 0
        foundMatch = False
        
        for char in key:
            num += ord(char)
            num = (num*17) % 256
        while index < len(boxes[num]):
            # print(f'{boxes[num][index][0]} == {key} => {boxes[num][index][0] == key}')
            if boxes[num][index][0] == key: # replace old lense with new one
                boxes[num][index][1] = value
                foundMatch = True
            
            index+=1
        if not foundMatch:
            boxes[num].append([key,value])
    
    print(f'{str} => {num%256}')

    # part1 += num 
# print(*boxes[0:5], sep='\n')
print(part1)
    
# score part 2
part2 = 0
for boxIndex in range (0,len(boxes)):
    for slotIndex in range (0,len(boxes[boxIndex])):
        part2 += (boxIndex+1)*(slotIndex+1)*boxes[boxIndex][slotIndex][1]
print(part2)
    
