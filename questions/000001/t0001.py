
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