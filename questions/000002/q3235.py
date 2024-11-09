from typing import List, Tuple, Optional
import math
class DSU:
    def __init__(self,N):
        self.p  = list(range(N))
        self.rank = [1]*N
    
    def find(self,x):
        if self.p[x] != x:
            self.p[x] =self.find(self.p[x])
        return self.p[x]
    
    def union(self,x,y):
        xr = self.find(x)
        yr = self.find(y)
        if self.rank[xr] <self.rank[yr]:
            xr,yr =yr,xr
        
        self.p[yr] = xr
        if self.rank[xr] == self.rank[yr]:
            self.rank[xr] += 1

class Solution:
    def canReachCorner(self, xCorner: int, yCorner: int, circles: List[List[int]]) -> bool:
        n = len(circles)
        p = [i for i in range(n+2)]
        rank= [1 ]*(n+2)
        def find(x):
            if p[x] != x :
                p[x] = find(p[x])
            return p[x] 

        def unino(x,y):
            a,b = find(x),find(y)
            if a == b:
                return
            if rank[a] < rank[b]:
                a,b = b,a 
            p[b] = a 
            if rank[a] == rank[b]:
                rank[a] +=1
        for i in range(n):
            a,b,r = circles[i]
            if ((abs(a) <=r and 0<=b<=yCorner) or ((abs(b-yCorner))<=r  and (0<=a<=xCorner))):
                unino(i,n)
            if ((abs(a-xCorner)<=r and (0<=b<=yCorner)) or (abs(b) <=r and (0<=a<=xCorner))) :
                unino(i,n+1)
            for j in range(n):
                a1,b1,r1= circles[j]
                if i ==j:continue

                xm,ym =(a*r1 +a1*r), (b*r1+b1*r)

                if (a-a1)**2 + (b-b1)**2 <= (r+r1)**2 and xm<xCorner*(r+r1) and ym<yCorner*(r+r1):
                    unino(i,j)
        def in_circle(x: int, y: int, cx: int, cy: int, r: int) -> int:
            return (x - cx) ** 2 + (y - cy) ** 2 <= r**2
        def cross_left_top(cx: int, cy: int, r: int) -> bool:
            a = abs(cx) <= r and 0 <= cy <= yCorner
            b = abs(cy - yCorner) <= r and 0 <= cx <= xCorner
            return a or b


        for a,b,r in circles:
            #print(a,b,r,in_circle(xCorner,yCorner,a,b,r))
           # print(cross_left_top(a,b,r))
            if in_circle(0,0,a,b,r) or in_circle(xCorner,yCorner,a,b,r):
                return False

        return find(n) != find(n+1)

re = Solution().canReachCorner( 5, 4, circles = [[5,6,4],[6,4,2],[2,5,4],[3,5,3]])
print(re) 