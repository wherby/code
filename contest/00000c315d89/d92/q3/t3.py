from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        pre = [0]*(n+1)
        for i in range(n):
            if customers[i] == "Y":
                pre[i+1] = pre[i] +1
            else:
                pre[i+1] = pre[i]
        mx =n+1
        ret =0
        allY = pre[n]
        for i in range(n+1):
            k = i - pre[i] +allY - pre[i]
            if k < mx:
                ret = i 
                mx = k 
        return ret




re =Solution().bestClosingTime("YYNY")
print(re)