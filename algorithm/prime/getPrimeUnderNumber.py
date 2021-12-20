import math
def getPrimes(n):
    visited = [0]*(n+1)
    for i in range(2,int(math.sqrt(n))+1):
        if visited[i] ==0:
            for j in range(i+i,n+1,i):
                visited[j] =1
    prims =[]
    for i in range(2,n+1):
        if visited[i] ==0:
            prims.append(i)
    return prims

ls = getPrimes(10**6)
#print(ls)
print(len(ls))
print(ls[:10])