from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
from collections import Counter
class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        primes=[2,3,5,7,11,13,17,19,23,29]
        dp=[0]*1024
        dp[0]=1
        no1 = 0
        mod = 10**9+7
        for a in nums:
            aa = a
            if a ==1:
                no1 +=1
            else:
                acc =0
                isG =True
                for i,b in enumerate(primes):
                    t = 0
                    while a %b ==0:
                        t +=1
                        a = a//b
                    if t >1:
                        isG =False 
                    if t %2 ==1:
                        acc +=1<<i
                if isG ==False:
                    continue
                ndp =[0]*1024
                
                for i in range(1024):
                    if i &acc ==0:
                        ndp[i^acc] = dp[i] 
                for i in range(1024):
                    dp[i] =  (ndp[i]+ dp[i])%mod
                #print(aa,acc,dp[:35],ndp[:35])
        #print(dp)
        sm =0
        mod = 10**9+7
        for i in range(1024):
            sm += dp[i]
        if no1 ==0:
            return (sm -1 + mod)%mod
        else:
            return (sm *(pow(2,no1,mod))-1+mod)%mod
            
        





re =Solution().squareFreeSubsets([26,6,4,27,6,18])
print(re)