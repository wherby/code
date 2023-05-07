# https://leetcode.cn/problems/3aqs1c/
from typing import List, Tuple, Optional
class Solution:
    def unSuitability(self, op: List[int]) -> int:
        mx = max(op)*2
        l,r = 1,mx
        while l<r:
            mid = (l+r)>>1
            acc =(1<<mid) -1
            alla =acc
            for a in op:
                acc = ((acc<<a) |(acc>>a))&alla
                #print(a,bin(acc))
            #print(bin(acc),mid)
            if acc ==0:
                l = mid +1
            else:
                r = mid 
        return l-1