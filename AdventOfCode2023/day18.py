test= False

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
        ySet = set([])
        for index in range(0,len(self.points)):
            ySet.add(self.points[index].y)
        
        yList = sorted(ySet)
        # print(sortedList)

        
        ##### Horz Lines Area #####
        for thisY in yList:
            # find all the x points at this y value 
            # then determine if there is a line, area, or gap between the points
            pointSet = set([])
            sliceArea = 0
            for pointIndex in range(0,len(self.points)-1):
                if thisY == self.points[pointIndex].y: 
                    if self.points[pointIndex].y == self.points[pointIndex+1].y:
                        # horz line found, add both x to the list
                        pointSet.add(self.points[pointIndex].x)
                        pointSet.add(self.points[pointIndex+1].x)
                elif thisY in range (min(self.points[pointIndex].y,self.points[pointIndex+1].y),max(self.points[pointIndex].y,self.points[pointIndex+1].y)) and \
                    self.points[pointIndex].x == self.points[pointIndex+1].x:
                    pointSet.add(self.points[pointIndex].x)
                    
            
            xList = sorted(pointSet)
            for xIndex in range (0,len(xList)-1):
                if self.contains(xList[xIndex]+1,thisY):
                    # print(f'Inside at {thisY} : {xList[xIndex]} -> {xList[xIndex+1]} => {xList[xIndex+1]-xList[xIndex] }')
                    sliceArea += xList[xIndex+1]-xList[xIndex] 
                else:
                    # print(f'Outside at {thisY} : {xList[xIndex]} -> {xList[xIndex+1]}')
                    sliceArea += 1 # to account for the line at the beginning / end
            # print(f'Slice area = {sliceArea + 1}')
            area+=sliceArea + 1

        ##### Horz Lines Area #####

        ##### Vertical Lines Area #####
        for yIndex in range(0,len(yList)-1):

            height = yList[yIndex+1] - yList[yIndex] - 1 
            width = 0
            # find all the vertical lines except for the last Y value
            lineSet = set([])
            for pointIndex in range(0,len(self.points)-1):

                minY = min(self.points[pointIndex].y,self.points[pointIndex+1].y)
                maxY = max(self.points[pointIndex].y,self.points[pointIndex+1].y)

                if maxY != minY and yList[yIndex] in range(minY,maxY+1) and yList[yIndex+1] in range(minY,maxY+1):
                    #vert line found, add X to the line list
                    lineSet.add(self.points[pointIndex].x)

            # in order add the area between the lines to the width
            lineList = sorted(lineSet)
            for lineIndex in range(0,len(lineList)-1,2):
                width += lineList[lineIndex+1] - lineList[lineIndex] +1

            # find the area in the shape between these lines not including the top and bottom                
            # print(f'{height}x{width} = {height*width}')
            area += height*width        
        ##### Vertical Lines Area #####
        return area 
x =0
y =0
myShape = Shape()
myShape.points.append(Coordinates(x,y))


for line in lines:
    strs = line.strip().split()
    # print(strs)
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

# part1=0

# debug = [[' ' for x in range(minX,maxX+1)] for y in range(minY,maxY+1)]

# for y in range(maxY,minY-1,-1):
#     str =''
#     for x in range(minX,maxX+1):
#         if myShape.contains(x,y):
#             part1+=1
#             debug[y][x] = '#'
#             str = str + '#'
#         else:
#             str = str + '.'
#     # print(str)
#     open('outputFile.txt', 'a').write(str+'\n')
# # debug[0][0]='X'
# # print(*debug,sep='\n')
# print(part1)


x =0
y =0
myShape2 = Shape()
myShape2.points.append(Coordinates(x,y))

for line in lines:
    strs = line.strip().split()
    distance = int(strs[2][2:-2],16)
    directionChar = strs[2][7]
    print(f'{strs} => {strs[2][2:-2]} : {distance} ; {directionChar}')
    match directionChar:
        case '0':
            x += distance
        case '1':
            y += -distance

        case '2':
            x += -distance
        case '3':
            y += distance
    myShape2.points.append(Coordinates(x,y))
print(myShape2.area())