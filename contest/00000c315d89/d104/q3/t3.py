from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        ls = [0]*60
        for a in nums:
            for i in range(32):
                if a %2 ==1 :
                    ls[i] +=1
                a = a //2
        mx =0
        #print(ls)
        for a in nums:
            ret =[]
            b = a 
            for i in range(32):
                if b %2 ==1:
                    ret.append(i)
                    ls[i] -=1
                b = b //2
            ret = [i+k for i in ret]
            s =[0]*60
            for i in ret:
                s[i] =1
            acc =0
            #print(ret,ls)
            for i in range(50,-1,-1):
                if s[i] >0 or ls[i] >0:
                    acc =acc*2+1
                else:
                    acc =acc*2
            mx = max(mx,acc)
            b = a 
            #print(b,a)
            for i in range(32):
                if b %2 ==1:
                    ls[i] +=1
                b = b //2
            #print(ls)
        return mx
        





re =Solution().maximumOr(nums = [12,9], k = 1)
print(re)