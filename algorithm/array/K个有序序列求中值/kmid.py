
from bisect import bisect_right,insort_left,bisect_left


def getMd(sa):
    acc =0
    #print(sa)
    acc+=1
    la=[]
    for i in range(n):
        if (1<<i) &sa:
            la.append(i)
    m = 0 
    for a in la:
        m +=len(lists[a])
    l = min(lists[a][0] for a in la)
    r = max(lists[a][-1] for a in la)
    while l <r:
        #print(l,r)
        md = (l+r)//2 
        cnt =0
        for a in la:
            cnt += bisect_right(lists[a] ,md)
        if cnt >= (m+1)//2:
            r = md 
        else:
            l = md+1
    #print(m,l,cnt,la)
    return m,l

lists = [[1,3,5],[2,4],[6,7,8]]
n = len(lists)

for state in range(1,2<<(n-1)):
    #print(state)
    print(getMd(state),state)
