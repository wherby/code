from typing import List, Tuple, Optional

from heapq import heapify,heappop,heappush 
class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(reverse= True)
        st = []
        dic = {}
        sm = 0
        mx  =0
        for i,item in enumerate(items):
            if i <k:
                if item[1] not in dic:
                    dic[item[1]] =1 
                else:
                    heappush(st,item[0])    
                sm += item[0]
            elif item[1] not in dic and st:
                sm -= heappop(st)
                sm += item[0]
                dic[item[1]] =1
            mx = max(mx,sm + len(dic)**2)
        return mx
