# OT
from typing import List, Tuple, Optional
from functools import cache
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        m = len(needs)
        

        @cache
        def dfs(state):
            if sum(state) ==0:
                return 0
            ret = 10**30
            for i,a in enumerate(price):
                if state[i]:
                    ns = list(state)
                    ns[i] -=1
                    ns = tuple(ns)
                    ret = min(ret, dfs(ns) + a)
            for sp in special:
                ls2 = sp[:m]
                c  = sp[-1]
                if all([a>=b for a,b in zip(state,ls2)]):
                    ns = [a-b for a,b in zip(state,ls2)]
                    ns = tuple(ns)
                    ret = min(ret,dfs(ns) + c)
            return ret
        return dfs(tuple(needs))
    
re = Solution().shoppingOffers(price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2])
print(re)