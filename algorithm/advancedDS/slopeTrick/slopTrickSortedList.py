# https://www.cnblogs.com/wyzwyz/p/14038855.html

from sortedcontainers import SortedList

def slopTrick(ls):
    ql,qr = SortedList([]),SortedList([])
    n = len(ls)
    lenN = [ls[i][1]-ls[i][0] for i in range(n)]
    ql.add(ls[0][0])
    qr.add(ls[0][0])
    ans = 0 
    addl,addr = 0,0
    for i in range(1,n):
        addl -= lenN[i]
        addr += lenN[i-1]
        L = ql[-1] + addl
        R = qr[0] + addr
        if ls[i][0]<L:
            ans += L-ls[i][0]
            ql.remove(ql[-1])
            ql.add(ls[i][0] - addl)
            ql.add(ls[i][0] - addl)
            qr.add(L -addr)
        elif ls[i][0] >R:
            ans += ls[i][0] - R 
            qr.remove(qr[0])
            qr.add( ls[i][0] -addr)
            qr.add(ls[i][0] - addr)
            ql.add(R-addl)
        else:
            ql.add(ls[i][0] - addl)
            qr.add( ls[i][0]-addr)
        #print(ans,addl,addr,L,R)
    return ans

