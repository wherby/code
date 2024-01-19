
res = []

def getNumber(x):
    if x == 2:
        res.append(2)
    elif x==3:
        res.append(3)
    else:
        getNumber(x//2)
        getNumber(x-x//2)

getNumber(2023)
#print(res)    
print(res.count(3),res.count(2))    





ls = [[1],[2],[3],[4],[5],[6]]
def getSnap(idx):
    mx = max(ls[:idx])
    return mx 



print(getSnap(3))
print(getSnap(-1))
print(getSnap(-4))
print()