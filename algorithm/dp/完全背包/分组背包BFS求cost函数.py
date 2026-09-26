# https://leetcode.cn/contest/weekly-contest-517/problems/minimum-operations-to-form-subset-sum-ii/description/
from collections import defaultdict,deque

class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        dp = [10**10] * (sum+1)
        dp[0] = 0 
        for a in nums:
            dic = {}
            q = deque()
            cur, cst = a, 0
            while cur > sum:
                cur //= 2
                cst += 1
            
            dic[cur] = cst
            q.append(cur)
            while q:
                u = q.popleft()
                d = dic[u]
                for v in (u * 2, u // 2):
                    if 0 <= v <= sum and v not in dic:
                        dic[v] = d + 1
                        q.append(v)
            ndp =list(dp)
            for k,v in dic.items():
                for f in range(sum, k-1,-1):
                    if dp[f-k] <10**10:
                        ndp[f] = min(ndp[f],dp[f-k]+v)
            dp =ndp 
        return -1 if dp[sum] ==10**10 else dp[sum]