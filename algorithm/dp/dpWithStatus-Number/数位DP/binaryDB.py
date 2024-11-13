#https://leetcode.cn/problems/count-k-reducible-numbers-less-than-n/description/

#前置条件处理  数位变形

from functools import cache


class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        mod = 10**9+7
        cands =[]
        n = len(s)
        dp = [0]*(n+1)
        cands.append(1)
        for i in range(2,n+1):
            dp[i] = dp[bin(i).count("1")] +1
            if dp[i]<k:
                cands.append(i)

        @cache
        def f(i,mask,is_limit,is_num):
            if i ==len(s):
                #print(mask)
                return not int(is_limit) if mask==0 else 0
            res =0
            if not is_num:
                res = f(i+1,mask,False,False) ##计算 0-9，10-99，100-999，1000-9999
            up = int(s[i]) if is_limit else 1
            for d in range(0 if is_num else 1, up +1):
                if d == 1 and mask ==0: continue
                res += f(i+1,mask-d,is_limit and d ==up, True)
            return res
        acc = 0
        for a in cands:
            if a > n:continue
            acc += f(0,a,True,False)
        f.cache_clear()
        return (acc)%mod
