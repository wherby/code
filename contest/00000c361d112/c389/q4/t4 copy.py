from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf
from bisect import bisect_right,insort_left,bisect_left
class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        cnt = 0
        n = len(nums)
        ls =[]
        for i,a in enumerate(nums):
            if a ==1:
                ls.append(i)
        if len(ls) ==0:
            return k*2
        m = len(ls)
        pls = [0]
        for a in ls:
            pls.append(pls[-1]+a)
        l = 0
        k -=1
        
        def getK(chages,i,k):
            acc = chages*2
            k -=chages
            l,r = 0,n
            while l <r:
                mid =(l+r)>>1
                left = bisect_left(ls,ls[i]-mid)
                right = bisect_right(ls,ls[i]+mid)
                #print(right,left)
                if right-left-1 <k:
                    l= mid+1
                else:
                    r = mid
                #print(right,left,mid,right-left-1 <k)
            #print(right,left,k,ls,mid,i)
            left = bisect_left(ls,ls[i]-l)
            right = bisect_right(ls,ls[i]+l)
            #print(right,left,l)
            if right-left-1  <k:
                return 10**20
            #print(acc,k)
            acc += pls[right]- pls[i+1] - ls[i] *(right-i-1)
            #print(acc,i,left,right,k)
            acc +=  ls[i]*(i-left+1)- (pls[i+1] -pls[left])
            #print("N",acc,left,i,ls[i]*(i-left),(pls[i+1] -pls[left+1]), pls[i+1] ,pls[left+1])
            return acc 
        mn  =10**20
        for i,a in enumerate(ls):
            cgs = min(k,maxChanges)
            mn = min(mn, getK(cgs,i,k))
            if cgs >0:
                mn = min(mn,getK(cgs-1,i,k))
            if cgs>1:
                mn = min(mn,getK(cgs-2,i,k))
        return mn
            





re =Solution().minimumMoves([1,0,1,0,1],3,0)
print(re)