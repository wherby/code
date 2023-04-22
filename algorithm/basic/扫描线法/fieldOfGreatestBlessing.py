# https://leetcode.cn/contest/season/2023-spring/problems/xepqZ5/
# 扫描线法 
from typing import List, Tuple, Optional



class Solution:
    def fieldOfGreatestBlessing(self, forceField: List[List[int]]) -> int:
        f = [(i*2,j*2,k*2) for i,j,k in forceField]
        ys = []
        
        for i,j,k in f:
            ys.append(j+k//2)
            ys.append(j-k//2)
            
        ys.sort()
        
        def cal(y):
            tmp = [i for i in f if i[1]-i[2]//2<=y<=i[1]+i[2]//2]
            q = []
            for i,j,k in tmp:
                q.append((i-k//2,1))
                q.append((i+k//2+1,-1))
            q.sort()
            ans = 0
            t = 0
            for i,k in q:
                t+=k
                ans = max(ans,t)
            return ans
        
        return max(cal(y) for y in ys)