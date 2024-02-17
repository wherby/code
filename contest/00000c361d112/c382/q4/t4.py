from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        #print(nums,k)
        ls = [0]*30
        for a in nums:
            for j in range(30):
                if (1<<(29-j)) &a:
                    ls[j] +=1
        isFind = False
        findJ = -1
        n = len(nums)
        for j in range(30):
            if ls[j] <=k and ls[j] >0 and n > ls[j]:
                k-=ls[j]
                ls[j] = 0 
                isFind = True
                findJ = j 
                break
        #print(k,findJ,ls[j])
        if isFind:
            tmp = []
            idx = 0
            while idx < n:
                a = nums[idx]
                idx +=1
                if a &(1<<(29-findJ)) ==0:
                    tmp.append(a)
                    
                elif len(tmp)==0:
                    st = []
                    st.append(a)
                    while idx<n and (nums[idx] &(1<<(29-findJ))):
                        st.append(nums[idx])
                        idx +=1
                    t = nums[idx]
                    idx +=1 
                    for a in st:
                        t = t &a 
                    tmp.append(t)
                else:
                    st = []
                    st.append(a)
                    while idx<n and (nums[idx] &(1<<(29-findJ))):
                        st.append(nums[idx])
                        idx +=1
                    if idx == n:
                        t = tmp.pop()
                        t = t&a 
                        tmp.append(t)
                    else:
                        t1 = (2<<30)-1
                        for a in st:
                            t1 = t1 &a 
                        if nums[idx] - t1&nums[idx] >= st[-1] -t1&st[-1]:
                            t = nums[idx]
                            idx +=1 
                            t = t &t1 
                            tmp.append(t)
                        else:
                            t = st.pop()
                            t = t1 &t
                            tmp.append(t)
            return  self.minOrAfterOperations(tmp,k)
        else:
            ret = 0 
            for j in range(30):
                if ls[j]:
                    ret += 1<<(29-j) 
            return ret




re =Solution().minOrAfterOperations(nums = [37,6,46,32,23],k=3)
re =Solution().minOrAfterOperations([7,3,15,14,2,8] ,4)
print(re)