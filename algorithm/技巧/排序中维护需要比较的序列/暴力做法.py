# https://leetcode.cn/problems/delete-columns-to-make-sorted-ii/
from typing import List, Tuple, Optional
from itertools import pairwise
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        res =["" for _ in range(n)]
        m = len(strs[0])
        cnt =0
        for j in range(m):
            isGood = True 
            tp = []
            for i in range(n):
                tp.append(res[i] +strs[i][j])
            for a,b in pairwise(tp):
                if a >b:
                    isGood = False
                    break
            if isGood:
                res = tp 
            else:
                cnt +=1
        return cnt