from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        acc =0
        n = len(nums)
        def isGood(idx):
            if 0<=idx<n and nums[idx] >=k:
                return True
            else:
                return False
        @cache
        def dfs(i,p):
            if i >=n:
                return 0
            mn = 10**20
            if isGood(i-2) or isGood(i-1) or isGood(i) or i <2:
                mn =min(mn, dfs(i+1,tuple([i,i-3,10**9] +nums[i-2:i])))
            else:
                if i>=2:
                    a = k - nums[i-2]
                    nums[i-2]=k
                    mn =min(mn, a + dfs(i+1,tuple([i,i-2,10**9] +nums[i-2:i])))
                    nums[i-2]-=a
                if i >=1:
                    a = k - nums[i-1]
                    nums[i-1] = k
                    mn = min(mn,a + dfs(i+1,tuple([i,i-1,10**9] +nums[i-2:i])))
                    nums[i-1] -=a
                a = k - nums[i]
                nums[i] =k
                mn = min(mn,dfs(i+1,tuple([i,i,10**9] +nums[i-2:i]))+a)
                nums[i] -=a
                # if i ==1:
                #     a = k - nums[i+1]
                #     nums[i+1] = k
                #     mn = min(mn,dfs(i+1)+a)
                #     nums[i+1] -=a
                # if i ==0:
                #     a = k-nums[i+2]
                #     nums[i+2] = k 
                #     mn = min(mn,dfs(i+1)+a)
                #     nums[i+2] -=a
            return mn
                
        return dfs(0,-3)   





re =Solution().minIncrementOperations(nums = [13,34,0,13,9,19],k=82)
#re= Solution().minIncrementOperations([2,3,0,0,2],4)
re =Solution().minIncrementOperations([6,14,17,4,7],22)
print(re)