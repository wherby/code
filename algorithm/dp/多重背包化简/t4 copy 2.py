# https://leetcode.cn/contest/biweekly-contest-115/problems/count-of-sub-multisets-with-bounded-sum/
# https://leetcode.cn/circle/discuss/maICM3/
# contest\00000c361d112\d115\q4\t4 copy 2.py
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
from collections import Counter



class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        dp =[0]*(r+1)
        dp[0] = 1
        c = Counter(nums)
        mod = 10**9+7
        for k,v in c.items():
            if k ==0:
                for i in range(r+1):
                    dp[i] = dp[i]*(v+1)
            else:
                ## 多重背包
                for i in range(k,r+1):
                    dp[i] = (dp[i] + dp[i-k])%mod
                ## 因为只能有 v个物品，所以要把 v+1以后的多重背包消掉
                for i in range(r,k*(v+1)-1,-1):
                    dp[i] = (dp[i] - dp[i-k*(v+1)])%mod
            #print(dp,dp2)
        return sum(dp[l:r+1])%mod




re =Solution().countSubMultisets(nums = [1,2,1,3,5,2], l = 3, r = 5)
print(re)