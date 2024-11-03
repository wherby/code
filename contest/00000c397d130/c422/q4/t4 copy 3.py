from typing import List, Tuple, Optional


from functools import cache

import math

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        mod = 10**9 +7
        n = len(num)
        ls = [0]*10
        for a in num:
            ls[int(a)]+=1
        sm = sum([int(a) for a in num])
        hfn = n //2
        hsm = sm //2
        if sm%2 ==1:
            return 0
        
        
        #print(cont([0]*10))
        pre = [0]
        for a in ls:
            pre.append(pre[-1]+a)

        @cache
        def dfs(i,idx,acc):
            if idx>hfn or acc > hsm:
                return 0
            if i ==10:
                if idx == hfn:
                    if acc == hsm:
                        return 1
                    return 0 
                return 0
            ret = 0
            for j in range(ls[i]+1):
                if n-hfn -(pre[i] -idx)>=0 and n-hfn -(pre[i] -idx) >=ls[i] -j:
                    ret += math.comb(hfn-idx,j) *dfs(i+1,idx+j,acc+j*i) *math.comb(n-hfn -(pre[i] -idx),ls[i] -j)
            return ret
        ret = dfs(0,0,0)%mod
        dfs.cache_clear()
        return ret



print(len("08961788077437553919640382583325637"))

re =Solution().countBalancedPermutations("123")
print(re)