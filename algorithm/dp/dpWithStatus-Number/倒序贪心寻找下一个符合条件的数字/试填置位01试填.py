# https://leetcode.com/contest/weekly-contest-486/problems/find-nth-smallest-integer-with-k-one-bits/description/
from typing import List, Tuple, Optional

import math
INF  = math.inf

class Solution:
    def nthSmallest(self, n: int, k: int) -> int:
        rest= n
        curk = k
        ans =0 
        for idx in range(60,-1,-1):
            if curk<=0:
                break
            if rest >math.comb(idx,curk):
                ans += 1<<idx
                rest -= math.comb(idx,curk)
                curk -=1

        return ans




re =Solution().nthSmallest(4,2)
print(re)