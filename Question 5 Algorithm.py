verticalOreCount = 0
verticalOreList = []
hortionzalOreCount = 0
HorizontalOreList = []
verticalCuts = []
horzCuts = []

heirs1  = 2
rows = 5
columns = 5
oreCount = 0

plan = [
    ['+','+','+','+','+'],
    ['+','+','+','+','+'],
    ['.','.','.','.','.'],
    ['.','.','.','.','.'],
    ['.','.','.','.','.']
]



for items in plan:
    for item in items:
        if item == '+':
            oreCount = oreCount + 1



for y in range(0,(columns)):
    for x in range(0,(rows)):
        if plan[x][y] == '+':
            verticalOreCount = verticalOreCount + 1
    verticalOreList.append(verticalOreCount)
    verticalOreCount = 0

Verticalbool = False
if(max(verticalOreList) <= oreCount/heirs1):
    Verticalbool = True
else:
    Verticalbool = False

if(Verticalbool is True):
    count = 0
    cuts = 0
    for idx in range(len(verticalOreList)):
        count += verticalOreList[idx]
        if(count == oreCount/heirs1):
            if(cuts == heirs1-1):
                break
            verticalCuts.append(idx+1)
            count = 0
            cuts += 1
    verticalCuts.append('-')

print(verticalCuts)