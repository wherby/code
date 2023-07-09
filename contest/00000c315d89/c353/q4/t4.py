from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        ls = deque([])
        acc = 0
        for i,a in enumerate(nums):
            if len(ls) ==k:
                acc -=ls[0]
                ls.popleft()
            b= a-acc
            acc +=b
            ls.append(b)
            #print(ls,i,a,acc)
        ls= list(ls)
        isGood =True
        for i in range(1,len(ls)):
            if ls[i] !=0:
                isGood =False
        return isGood




#re =Solution().checkArray(nums = [2,2,3,1,1,0], k = 3)
re = Solution().checkArray([60,72,87,89,63,52,64,62,31,37,57,83,98,94,92,77,94,91,87,100,91,91,50,26],4)
#re = Solution().checkArray([24,24,14,37,31,88,94,38,94,0,100,100,4,46,5,50,0,33,22,25,0],10)
print(re)