# https://leetcode.cn/contest/weekly-contest-508/problems/filter-occupied-intervals/description/
# 用差分标记去除
from typing import List, Tuple, Optional

class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:
        ls = []
        occupiedIntervals.sort()
        curS = occupiedIntervals[0][0]
        curE = occupiedIntervals[0][1]+1
        for s,e in occupiedIntervals:
            if s > curE:
                ls.append([curS,curE-1]) 
                curS = s 
                curE = e+1
            else:
                curE= max(curE,e +1)
        ls.append([curS,curE-1])
        dp = []
        for s,e in ls:
            dp.append((s,+1))
            dp.append((e+1,-1))
        dp.append((freeStart,-1))
        dp.append((freeEnd+1,+1))
        dp.sort()
        cur = 0
        curs = -1
        ret = []

        for s,op in dp:
            cur += op 
            if cur >0:
                curs = s 
            elif cur ==0 and op ==-1:
  
                ret.append([curs,s-1])

        return ret