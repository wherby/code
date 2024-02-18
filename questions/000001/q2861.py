from typing import List, Tuple, Optional

class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        mx = 0
        def verify(n1,k):
            ret = 0 
            for i,a in enumerate(composition[k]):
                ret += max(0,a*n1 - stock[i])*cost[i]
            return ret <= budget
        for i in range(k):
            l,r = 0,10**8
            while l <r:
                mid = (l+r+1)>>1
                if verify(mid,i):
                    l = mid
                else:
                    r= mid -1
            mx = max(mx,l)
        return mx
            

re =Solution().maxNumberOfAlloys(n = 3, k = 2, budget = 15, composition = [[1,1,1],[1,1,10]], stock = [0,0,100], cost = [1,2,3])
print(re)