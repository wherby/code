
from typing import List, Tuple, Optional
from collections import defaultdict,deque
from math import inf

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        cnt = defaultdict(lambda: defaultdict(int))
        cnt2= defaultdict(lambda: defaultdict(int))
        bls = []
        for i,(x,y) in enumerate(points):
            for x2,y2 in points[:i]:
                dx = x-x2 
                dy = y -y2 
                if dx ==0:
                    k =inf 
                    b =x
                else:
                    k = dy/dx 
                    b = y -k*x 
                    bls.append(b)
                cnt[k][b] += 1 
                cnt2[(x+x2,y+y2)][k] +=1 

        ans = 0 
        for ct in cnt.values():
            s = 0 
            for c in ct.values():
                ans += s*c 
                s += c 
        for ct in cnt2.values():
            s = 0 
            for c in ct.values():
                ans -= s*c 
                s +=c 
        print(bls)
        return ans 

from input import points
re = Solution().countTrapezoids(points)
print(re)