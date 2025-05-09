from functools import cache
import math

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        mod = 10**9 +7
        num = [int(a) for a in num]
        n = len(num)
        ls = [0]*10
        for a in num:
            ls[a]+=1
        if sum(num)%2 ==1 :
            return 0 
        m = len(num)
        hfN = m//2
        hf = sum(num)//2
        pre =[0]
        for a in ls:
            pre.append(pre[-1]+a)
        @cache
        def dfs(idx,resN,res):
            if idx ==10:
                return int(res == 0 and resN ==0)
            ret = 0
            res2 = n - hf -(pre[idx]-(hf-resN))
            if res2 <0:
                return 0
            for i in range(min(resN,ls[idx])+1):
                if i*idx <= res:
                    ret += dfs(idx+1, resN -i ,res - i*idx)* math.comb(resN,i)*math.comb(res2,ls[idx]-i)
                    
            return ret %mod
        return dfs(0,hfN,hf)
