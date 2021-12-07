def addx(x):
    while x < 1024:
        print(x,x&-x)
        x += (x & -x)
        
#addx(1)
addx(5)
print("===")
addx(513)
print("===")

def getX(x):
    while x>0:
        print(x)
        x -=(x & -x)
getX(5)
