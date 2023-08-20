# https://leetcode.cn/problems/maximize-the-profit-as-the-salesman/description/
from typing import List, Tuple, Optional


from sortedcontainers import SortedDict,SortedList

class MonoStack:
    def __init__(self) -> None:
        self.ls = SortedList([])
    
    def inSert(self,key,value):
        idx= self.ls.bisect_left((key,0))
        rmlst = []
        for i in range(idx,len(self.ls)):
            if self.ls[i][1]<=value:
                rmlst.append(self.ls[i])
        for item in rmlst:
            self.ls.remove(item)
        if len(self.ls) == 0 or self.ls[idx-1][1]<value:
            self.ls.add((key,value))
    
    def find(self,key):
        idx = self.ls.bisect_left((key,10**30))
        return self.ls[idx-1][1] if idx-1>=0 else 0

class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers.sort(key=lambda x:x[1])
        nst = MonoStack()
        for a,b,c in offers:
            nst.inSert(b,c+ nst.find(a-1))
        return nst.find(offers[-1][1])




re =Solution().maximizeTheProfit(4,[[1,3,9],[0,2,10],[1,3,3],[0,1,3],[2,2,1],[3,3,7],[2,2,1],[1,2,9],[1,2,8]])
print(re)