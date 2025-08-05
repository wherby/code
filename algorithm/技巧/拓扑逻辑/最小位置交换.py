# https://leetcode.cn/problems/rearranging-fruits/?envType=daily-question&envId=2025-08-02
from typing import List, Tuple, Optional
from collections import defaultdict,deque
from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        c = Counter(basket1+basket2)
        for k,v in c.items():
            if v %2 == 1:
                return -1 
        c1 = Counter(basket1)
        ls1,ls2 = [],[]
        for k,v in c.items():
            hf = v //2 
            t1 = hf - c1[k]
            if t1>0:
                ls1.extend([k]*t1)
            elif t1 <0:
                ls2.extend([k]*(-t1))
        ls1.sort()
        ls2.sort()
        cnt = 0 
        dq1 =deque(ls1)
        dq2 = deque(ls2)
        mn = min(basket1+basket2)
        while dq1:
            if dq1[0]> dq2[0]:
                dq1,dq2 = dq2,dq1
            cnt += min(dq1[0],mn*2)
            dq1.popleft()
            dq2.pop()
        
        return cnt

re= Solution().minCost([84,80,43,8,80,88,43,14,100,88],[32,32,42,68,68,100,42,84,14,8])
print(re)