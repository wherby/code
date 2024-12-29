def getAllDividerN(MAX):
    
    fac= [[] for _ in range(MAX)]
    for i in range(1,MAX):
        for j in range(i,MAX,i):
            fac[i].append(j)
    return fac

fac = getAllDividerN(201)
print(fac[:20])


def getAllDivN(MAX):
    fac = [[] for _ in range(MAX)]
    for i in range(1,MAX):
        for j in range(i,MAX,i):
            fac[j].append(i)
    return fac 
fac2 = getAllDivN(20001)
print(fac2[:20])