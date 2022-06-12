# https://leetcode.com/contest/weekly-contest-297/problems/fair-distribution-of-cookies/

from functools import cache
from math import inf


class Solution:
    def distributeCookies(self, cookies, k: int) -> int:
        n = len(cookies)
        
        @cache
        def rec(mask,k):
            if mask ==0:
                return 0
            if k ==0:
                return inf
            ans = inf 
            orig = mask 
            while mask:
                mask = orig & mask-1 #remaining bits
                amt = sum(cookies[i] for i in range(n) if (orig^mask) & 1<<i)
                ans = min(ans,max(amt,rec(mask,k-1)))
            return ans
        return rec((1<<n)-1,k)

re =Solution().distributeCookies(cookies = [8,15,10,20,8], k = 2)
print(re)