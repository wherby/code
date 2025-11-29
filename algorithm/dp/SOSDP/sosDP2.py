# https://leetcode.com/contest/weekly-contest-477/problems/number-of-effective-subsequences/description/
# 为了求 N(all) 则需要用容斥原理
# 假如 all = 111        N(111) = dp[111] - dp[110]-dp[101] -dp[011] + dp[001]+dp[010]+dp[100] - dp[000]
        # for t in range(1<<m):
        #     op = bin(t).count("1")%2 
        #     op = 1 if op else -1 
    
        #     ret += pow(2,dp[t^all],mod)*op
# 上面一段代码，是为了解决 DP[all] 的反数， 如果 t 的1 的位数是奇数个，则对应的状态t^all的数量应该在全集里减去
# 因为 题目需要求的是 AllComb - N(all) => 所以op 在t的1 是奇数个的时候，反号

from typing import List, Tuple, Optional
from collections import defaultdict,deque
class Solution:
    def countEffective(self, nums: List[int]) -> int:
        mod = 10**9+7
        sm = 0 
        n = len(nums)
        for a in nums:
            sm = sm| a 
        idx = [i for i in range(32) if (1<<i)&sm]
        m = len(idx)
        dic = defaultdict(int)
        for num in nums:
            acc = 0 
            for i,a  in enumerate(idx):
                if (1<<a)&num:
                    acc|= 1<<i
            dic[acc] +=1
        dp = [0]*(1<<m)
        for k,v in dic.items():
            dp[k] = v
        u = 1<<m
        for i in range(m):
            bit = 1<<i
            s = 0 
            while s <u:
                s |= bit  # 快速跳到第 i 位是 1 的 s
                dp[s] += dp[s^bit]
                s +=1
        ret = pow(2,n,mod)
        all=u-1
        for t in range(1<<m):
            op = bin(t).count("1")%2 
            op = 1 if op else -1 
    
            ret += pow(2,dp[t^all],mod)*op
            #print(op,t,dp[t])
        return ret%mod