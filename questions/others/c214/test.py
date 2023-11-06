def addx(x):
    while x < 1000:
        print(x)
        x += (x & -x)
        
#addx(1)
addx(5)

def getX(x):
    while x>0:
        print(x)
        x -=(x & -x)
getX(5)
