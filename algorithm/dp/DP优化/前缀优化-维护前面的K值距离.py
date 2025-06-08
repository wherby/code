# https://leetcode.cn/contest/weekly-contest-453/problems/count-partitions-with-max-min-difference-at-most-k/description/
from typing import List, Tuple, Optional

from collections import defaultdict,deque
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod =10**9+7
        n = len(nums)
        dp = [0]*(n+1)
        dp[0] = 1
        pre = [0]*(n+2)
        pre[1] = 1 
        left = 0 
        minQ,maxQ = deque([]),deque([])
        for i in range(n):
            while minQ and nums[i] < nums[minQ[-1]]:
                minQ.pop()
            minQ.append(i)
            while maxQ and nums[i] > nums[maxQ[-1]]:
                maxQ.pop()
            maxQ.append(i)
            while nums[maxQ[0]] - nums[minQ[0]] >k:
                left +=1 
                while minQ[0] < left :
                    minQ.popleft()
                while maxQ[0] < left:
                    maxQ.popleft()
            dp[i+1] = (pre[i+1] -pre[left ])%mod 
            pre[i+2] = (pre[i+1] + dp[i+1])%mod 
            #print(dp,pre,left)
        return dp[n] 



re =Solution().countPartitions(nums = [9,4,1,3,7], k = 4)
print(re)