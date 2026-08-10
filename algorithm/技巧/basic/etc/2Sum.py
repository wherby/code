# 2Sum 变体
from typing import List, Tuple, Optional
from collections import Counter
from collections import defaultdict,deque
class Solution:
    def maximumWidth(self, planks: list[int]) -> int:
        c = Counter(planks)
        keys = list(c.keys())
        m = len(keys)
        c2 = defaultdict(int)
        for  i in range(m):
            a = keys[i]
            ca = c[a]
            for j in range(i+1,m):
                b = keys[j]
                cb = c[b]
                c2[a+b] += min(ca,cb)
        for a,ca in c.items():
            c2[a*2] += ca//2 
        cand = set(list(c.keys()) + list(c2.keys()))
        ret = 0
        for  h in cand:
            cur = c[h] + c2[h]
            ret = max(ret,cur)
        return ret     