# https://leetcode.cn/contest/weekly-contest-336/problems/minimum-time-to-complete-all-tasks/
from typing import List, Tuple, Optional

class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        ls=[0]*2002
        tasks.sort(key=lambda x: x[1])
        for s,e,c in tasks:
            tss = sum(ls[s:e+1])
            if tss >=c:
                continue
            c -=tss
            for i in range(e,s-1,-1):
                if ls[i]==0 and c>0:
                    c-=1
                    ls[i]=1
            #print(s,e,c,ls[:20])
        return sum(ls)