

test= True
lines = open("C:\\Users\\Ben\\Workspace\\PublicShare\\AdventOfCode2023\\test.txt").readlines() if test \
    else open('C:\\Users\\Ben\\Workspace\\PublicShare\\AdventOfCode2023\\day18.txt').readlines() 

class Coordinates:
    def __init__(self,xIn: int, yIn: int):
        self.x = xIn
        self.y = yIn

class Shape:
    def __init__(self):
        self.points = [Coordinates(0,0) for y in range (0,0)]
    def contains(self, x: int, y:int):
        leftCount = 0
        for index in range(0,len(self.points)-1):
            pointA = self.points[index]
            pointB = self.points[index+1]            
            if pointA.x == pointB.x: # vertical line
                if y > min(pointA.y,pointB.y) and y <= max(pointA.y,pointB.y): # within bounds of the line
                    if x == pointA.x:
                        return True # point on the line is in the shape
                    if x > pointA.x:
                        leftCount += 1 # point is right of the line
            else: # horizontal  line
                if y == pointA.y and x >= min(pointA.x,pointB.x) and x <= max(pointA.x,pointB.x):
                    return True #point is on the line, return true
        return leftCount % 2 == 1 # if an odd number of lines are to the left, the point is in the shape
        return False
    def area(self):
        # makes horizontal slices at each corner
        # determine the lines that are in the slice
        # determine the area between the lines
        area = 0
        yList = set([])
        for index in range(0,len(self.points)):
            yList.add(self.points[index].y)
        
        sortedList = sorted(yList)
        # print(sortedList)

        # firstLine =1 # accounts for the line on the edge
        for index in range(0,len(sortedList)-1):
            # list the x indexes in this range
            xList = set([])
            height = sortedList[index+1] - sortedList[index] -1
            firstLine = 0            
            for pointIndex in range(0,len(self.points)-1):
                minP = min(self.points[pointIndex].y,self.points[pointIndex+1].y)
                maxP = max(self.points[pointIndex].y,self.points[pointIndex+1].y)
                # if vert line and 
                if maxP != minP and sortedList[index] in range(minP,maxP+1) and sortedList[index+1] in range(minP,maxP+1):
                    #vert line found, add x to the list
                    xList.add(self.points[pointIndex].x)
                elif sortedList[index+1] == minP and minP == maxP: # store hoz length
                    finalLineLength = max(self.points[pointIndex].x,self.points[pointIndex+1].x) - min(self.points[pointIndex].x,self.points[pointIndex+1].x) +1
            sortedXList = sorted(xList)  

            if(len(sortedXList) )%2 ==1:
                print("***************************************************ODD LEN") 
            width = 0
            print(sortedXList)
            for pointIndex in range(0,len(sortedXList),2):
                width += sortedXList[pointIndex+1] - sortedXList[pointIndex] + 1
                   
            area += height*width #+ lineLength#+ max(bigSet) - min(bigSet) +1
            print(f'{height}x{width} = {height*width} ')#+ {lineLength}')
        
        #TODO find a way to account for where the vertical lines are

        return area + finalLineLength
x =0
y =0
myShape = Shape()
myShape.points.append(Coordinates(x,y))


for line in lines:
    strs = line.strip().split()
    print(strs)
    match strs[0]:
        case 'U':
            y += int(strs[1])
        case 'D':
            y += -int(strs[1])

        case 'L':
            x += -int(strs[1])
        case 'R':
            x += int(strs[1])
    myShape.points.append(Coordinates(x,y))

print(myShape.area())

minX = myShape.points[0].x
maxX = minX
minY = myShape.points[0].y
maxY = minY

# print(len(myShape.points))

for point in myShape.points:
    # print(f'{point.x}:{point.y}')
    minX = min(minX,point.x)
    maxX = max(maxX,point.x)
    minY = min(minY,point.y)
    maxY = max(maxY,point.y)
# print(f'{minX}:{minY} :: {maxX}:{maxY}')

part1=0

debug = [[' ' for x in range(minX,maxX+1)] for y in range(minY,maxY+1)]

for y in range(maxY,minY-1,-1):
    str =''
    for x in range(minX,maxX+1):
        if myShape.contains(x,y):
            part1+=1
            debug[y][x] = '#'
            str = str + '#'
        else:
            str = str + '.'
    # print(str)
    open('outputFile.txt', 'a').write(str+'\n')
# debug[0][0]='X'
# print(*debug,sep='\n')
print(part1)

