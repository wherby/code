def doSomething(st):
    print(st)

def getSub(state):
    subset =state
    while subset>0:
        doSomething(subset)
        subset = (subset)-1 &state

getSub(7)
getSub(5)