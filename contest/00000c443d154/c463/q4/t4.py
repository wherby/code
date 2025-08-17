# https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/submissions/
from typing import List, Tuple, Optional

from collections import defaultdict,deque

from functools import reduce
from operator import xor
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        BIG = 100
        qrs = defaultdict(list)
        mod = 10**9+7
        for l,r,k,v in queries:
            if k >=BIG:
                for j in range(l,r+1,k):
                    nums[j] = (nums[j]*v)%mod
            else:
                qrs[k].append((l,r,k,v))
        
        for k in range(1,BIG+1):
            
            acc = [[] for _ in range(n+k)] 
            if k not in qrs:
                continue
            for l,r,k,v in qrs[k]:
                acc[l].append(v)
                lst=(r-l)//k*k  + l +k
                acc[lst].append(-v)
            ac  =[1]*(n+k)
            for i in range(n):
                t = ac[i-k]
                for b in acc[i]:
                    if b > 0:
                        t *= b
                        t = t%mod
                    else:
                        t =t* pow(-b,-1,mod)
                ac[i] = t 
            for i in range(n):
                nums[i] = (nums[i]*ac[i])%mod 
            #print(nums,ac,acc)
        return reduce(xor,nums)




re =Solution().xorAfterQueries( nums = [2,3,1,5,4], queries = [[1,4,2,3],[0,2,1,2]])
re =Solution().xorAfterQueries( nums = [931,810,289], queries = [[0,1,3,1],[1,2,1,14],[1,1,3,14],[2,2,3,4],[2,2,1,6]])
print(re)