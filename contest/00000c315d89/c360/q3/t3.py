from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        if sum(nums) < target:
            return -1
        dic = defaultdict(int)
        dic2 = defaultdict(int)
        for i in range(32):
            b = 1<<i
            dic[b] =i
        for a in nums:
            dic2[dic[a]] +=1
        st=bin(target)[2:]
        st= [int(a) for a in st]
        acc = 0
        m  = len(st)
        cnt =0
        #print(st)
        for i in range(m):
            a = m-1-i
            if st[a] ==1:
                #print(i,st[a],a,acc,dic2)
                if dic2[i] ==0 and acc <(1<<i):
                    #print("aa",i)
                    #print(i,st[a],a,acc,dic2)
                    for j in range(i+1,32):
                        if dic2[j] >=1:
                            
                            dic2[j] -=1
                            for k in range(i,j):
                                dic2[k] +=1
                                cnt +=1
                            break
                else:
                    dic2[i] -=1
            acc += dic2[i] <<i
        return cnt
            




re =Solution().minOperations(nums = [1,32,1,2], target = 12)
print(re)