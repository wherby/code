def getAllDiv(n):
    visited=[0]*(n+2)
    res =[]
    for i in range(2,n+1):
        if visited[i]: continue
        res.append(i)
        for j in range(i,n+1,i):
            visited[j] =1
    def getAllComb(pls,n):
        ret =[]
        for p in pls:
            while n%p ==0:
                ret.append(p)
                n = n//p 
        return ret
    allC = getAllComb(res,n)
    ret =set([])
    for i in range(2<<len(allC)):
        acc =1
        for j in range(len(allC)):
            if (1<<j) &i :
                acc *= allC[j]
        ret.add(acc)
    return ret

print(getAllDiv(10))