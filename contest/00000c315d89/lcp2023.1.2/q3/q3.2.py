# https://leetcode.cn/contest/season/2023-spring/problems/kjpLFZ/
# using dijstra will timeout 

from typing import List, Tuple, Optional


from typing import List, Tuple, Optional
from collections import defaultdict,deque


class Solution:
    def extractMantra(self, mtx: List[str], mantra: str) -> int:
        m,n = len(mtx),len(mtx[0])
        st = deque([(0,0,0)])
        visit={}
        N= len(mantra)
        steps= 0
        while st:
            q= []
            for idx,x,y in st:
                if (idx,x,y) in visit:continue 
                visit[(idx,x,y)] =1
                if idx ==N:return steps 
                if mtx[x][y] == mantra[idx]:
                    q.append((idx+1,x,y))
                else:
                    for a,b in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                        if 0<=a<m and 0<=b<n and (idx,a,b) not in visit:
                            q.append((idx,a,b))
            st = q 
            steps +=1
        return -1

re = Solution().extractMantra(["sd","ep"],  "speed")
print(re)