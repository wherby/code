# https://leetcode.com/contest/weekly-contest-315/problems/count-subarrays-with-fixed-bounds/
## https://leetcode.com/problems/count-subarrays-with-fixed-bounds/solutions/2708099/java-c-python-sliding-window-with-explanation/

from typing import List, Tuple, Optional

class Solution:
    def countSubarrays(self, A: List[int], minK: int, maxK: int) -> int:
        res = 0
        jmin = jmax = jbad = -1
        for i,a in enumerate(A):
            if not minK <= a <= maxK: jbad = i
            if a == minK: jmin = i
            if a == maxK: jmax = i
            res += max(0, min(jmin, jmax) - jbad)
        return res
        

