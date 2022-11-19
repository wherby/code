# https://leetcode.com/contest/biweekly-contest-81/problems/number-of-distinct-roll-sequences/
# contest/00000c275d69/d81/q4
# 


import math
class Solution:
    def distinctSequences(self, n: int) -> int:
        dp= [[0]*343 for _ in range(n)]
        for i in range(1,7):
            dp[0][i] =1
        changes =[[] for _ in range(343)]
        for i in range(343):
            i1 = i%7 
            i2 = i//7%7 
            i3 = i//7//7 
            if i1 ==0: continue
            if i2 >0 and (i1 ==i2 or math.gcd(i1,i2) !=1): continue
            if i3 >0 and (i2 == i3  or math.gcd(i2,i3) != 1):continue
            for k in range(1,7):
                if k == i1 or k ==i2 or math.gcd(i1,k) != 1 : continue
                t = i1 *7 + i2 *7 *7  + k 
                changes[t].append(i)
        keys = []
        for i,a in enumerate(changes):
            if len(a)>0:
                keys.append(i)
        #print(changes)
        mod  = 10**9+7
        for i in range(1,n):
            for j in keys:
                for k in changes[j]:
                    dp[i][j] += dp[i-1][k]
                    dp[i][j] %=mod
        return sum(dp[n-1])%mod

re = Solution().distinctSequences(20)
print(re)
                