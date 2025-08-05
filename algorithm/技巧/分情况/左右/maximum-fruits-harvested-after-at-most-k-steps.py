# https://leetcode.cn/problems/maximum-fruits-harvested-after-at-most-k-steps/?envType=daily-question&envId=2025-08-03
from typing import List, Tuple, Optional

from bisect import bisect_right,insort_left,bisect_left


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        ps = []
        pls = [0]
        for p,a in fruits:
            ps.append(p)
            pls.append(a+pls[-1])
        mx = 0 
        for i,p in enumerate(ps):
            if abs(p-startPos)>k:
                continue
            if p >= startPos:
                l = startPos
                r = startPos + k 
                
            else:
                l = p 
                r = max(startPos,k-(startPos-l) + l , startPos + (k-(startPos-l))//2)
            ridx = bisect_right(ps,r)
            lidx = bisect_left(ps,l)
            mx = max(mx,pls[ridx] -pls[lidx])
        return mx