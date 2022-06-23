#https://leetcode.cn/problems/cut-off-trees-for-golf-event/
from collections import defaultdict,deque
class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        m,n = len(forest),len(forest[0])
        
        def bfs(fx,fy,tx,ty):
            q =deque([(0,fx,fy)])
            vist={(fx,fy):1}
            while q:
                d,x,y = q.popleft()
                if x == tx and y == ty:
                    return d
                for nx,ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                    if 0<=nx<m and 0<=ny<n and forest[nx][ny] and (nx,ny) not in vist:
                        vist[(nx,ny)]=1
                        q.append((d+1,nx,ny))
            return -1
            
        fl = [(h,i,j) for i,row in enumerate(forest)  for j,h in enumerate(row)if h>1]
        fl.sort()
        ans = 0
        cx,cy=0,0
        for _,i,j in fl:
            d = bfs(cx,cy,i,j)
            if d < 0:
                return -1
            ans += d 
            cx,cy = i,j
        return ans