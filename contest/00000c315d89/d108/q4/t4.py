from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        ta = (m-1)*(n-1)
        dic = {}
        for a,b in coordinates:
            dic[(a,b)]=1
        ret = [0]*5
        visit = {}
        for a,b in coordinates:
            
            for a1,b1 in (a-1,b-1),(a-1,b),(a-1,b+1),(a,b-1),(a,b),(a,b+1),(a+1,b-1),(a+1,b),(a+1,b-1):
                if (a1,b1) in visit: continue
                if 0<=a1<m-1 and 0<=b1<n-1:
                    visit[(a1,b1)] =1
                    acc=0
                    if a1 == m-1 or b1 == n-1:continue
                    for c,d in (a1,b1),(a1+1,b1),(a1,b1+1),(a1+1,b1+1):
                        if (c,d) in dic:
                            acc +=1
                    ret[acc] +=1
        ret[0] = 0
        #print(ta,sum(ret),ret)
        ret[0]= ta - sum(ret)
        
        return ret
        



m=32
n=32
coordinates=[[17,29],[29,16],[19,20],[18,9],[16,7],[20,25],[22,19],[4,9],[14,17],[6,23],[2,2],[20,1],[8,7],[4,7],[14,14],[10,10],[1,27],[18,23],[6,30],[8,18],[26,23],[25,8],[5,6],[3,4]]
re =Solution().countBlackBlocks(m , n , coordinates )
print(re)