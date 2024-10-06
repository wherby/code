from collections import defaultdict,deque
def getSubListUnderN(n):
    ret = [[] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(i,n+1,i):
            ret[j].append(i)
    return ret

d = getSubListUnderN(100000)
print(d[100])
print(d[102])
    