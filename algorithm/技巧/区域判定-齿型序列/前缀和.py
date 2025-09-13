from typing import List, Tuple, Optional

class Presum2d:
    def __init__(self,arr):
        m,n = len(arr),len(arr[0])
        self.pre = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                #print(i,j,m,n)
                self.pre[i+1][j+1] = self.pre[i][j+1] + self.pre[i+1][j] -self.pre[i][j] + arr[i][j]
    
    def query(self,x1,y1,x2,y2):
        a = self.pre[x2+1][y1]
        b = self.pre[x1][y2+1]
        c = self.pre[x1][y1]
        return self.pre[x2+1][y2+1] -a -b +c
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort()
        xs,ys = set(),set()
        for a,b in points:
            xs.add(a)
            ys.add(b)
        xs,ys = sorted(list(xs)),sorted(list(ys))
        dicx={}
        dicy = {}
        for i,a in enumerate(xs):
            dicx[a] = i 
        for i,a in enumerate(ys):
            dicy[a] =i  
        ps = []
        for a,b in points:
            ps.append([dicx[a],dicy[b]])
        points = ps
        N = len(ps) +1
        arr=[[0]*N for _ in range(N)]
        for a,b in points:
            arr[a][b] = 1
        pre = Presum2d(arr)
        cnt = 0 
        n = len(points)
        for i in range(n):
            x2,y1 = points[i]
            for j in range(n):
                x1,y2 = points[j]
                if x1 <=x2 and y1<=y2 and pre.query(x1,y1,x2,y2) ==2:
                    cnt +=1
                #print(x1,y1,x2,y2,pre.query(x1,y1,x2,y2))
        return cnt