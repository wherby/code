from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num)
        ls = [int(a) for a in num ]
        mx =n
        state =0
        cnt =0
        for a in ls[::-1]:
            if state ==0:
                if a == 0:
                    state =1
                else:
                    cnt  +=1
            else:
                if a ==0 or a == 5:
                    mx = min(mx,cnt)
                else:
                    cnt +=1 
        mx = min(mx,cnt)   
        state =0
        cnt =0
        for a in ls[::-1]:
            if state ==0:
                if a ==5:
                    state =1   
                else:
                    cnt +=1
            else:
                if a ==2 or a ==7:
                    mx = min(mx,cnt)
                else:
                    cnt +=1
        return mx 





re =Solution().minimumOperations("10")
print(re)