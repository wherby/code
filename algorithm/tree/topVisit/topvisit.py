# ./pic/topvisit.png
from collections import deque

def visit(a):
    print(a)

def topvisit(g,d):
    q=deque([])
    for i,a in enumerate(d):
        if a ==0:
            q.append(i)
    while q:
        x =q.popleft()
        visit(x)
        for a in g[x]:
            d[a] -=1
            if d[a] ==0:
                q.append(a)
        
        
        
