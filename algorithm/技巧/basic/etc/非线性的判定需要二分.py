# https://leetcode.cn/problems/minimum-initial-strength-to-defeat-all-monsters/
# 这里的每个计算之后的值是非线性变化的，但是满足条件的值是单向的，所以可以2分找到临界值

class Solution:
    def minInitialStrength(self, monsters: list[int], boosts: list[list[int]]) -> int:
        n = len(monsters)
        
        dp =[0]*(n+1)
        for l,r,v in boosts:
            dp[l] +=v
            dp[r+1] -=v 
        pls = [0]*n 
        cur = 0 
        for i in range(n):
            cur += dp[i]
            pls[i] = cur 
        l,r = 0,sum(monsters)
        def verify(mid):
            cur =mid 
            for i in range(n):
                if cur + pls[i] < monsters[i]:
                    return False
                cur = max(0,cur -monsters[i])
            return True
        while l<r:
            mid = (l+r)>>1
            if verify(mid):
                r =mid
            else:
                l= mid +1
        return l