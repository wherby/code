# https://leetcode.cn/problems/closest-dessert-cost/
from typing import List, Tuple, Optional
from bisect import bisect_right,insort_left,bisect_left
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        target= target-0.001  ## 对target减去一个小数 达到优先选择左边的目的
        n = len(toppingCosts)
        ls = []
        for i in range(3**n):
            acc =0
            t = i
            for j in range(n):
                k  = t %3 
                t = t //3 
                acc += toppingCosts[j]*k 
            ls.append(acc)
        ls.sort()
        baseCosts.sort()
        ret =baseCosts[0]
        mn = target-ret
        for a in baseCosts:
            k = bisect_left(ls,target-a)
            if k ==0:
                t = abs(target-a - ls[0])
                if t < mn:
                    mn = t 
                    ret = a + ls[0]
            elif k == len(ls):
                t = abs(target-a-ls[-1])
                if t < mn:
                    mn = t 
                    ret = a + ls[-1]
            else:
                t = abs(target-a - ls[k-1])
                if t < mn:
                    mn = t 
                    ret = a + ls[k-1]
                t = abs(target-a -ls[k])
                if t <mn:
                    mn = t 
                    ret = a+ ls[k]
            #print(a,ret,k,ls)
        return ret


re =Solution().closestCost([2,9,10,5,4,9,8,8,1],[9,3,10,9],3)
print(re)