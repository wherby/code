#  https://leetcode.cn/problems/moving-stones-until-consecutive-ii/submissions/
from typing import List, Tuple, Optional
class Solution:
    def numMovesStonesII(self, s: List[int]) -> List[int]:
        s.sort()
        n = len(s)
        a1 = s[-2] -s[0]-n +2
        a2 = s[-1]-s[1] -n +2
        mx = max(a1,a2)
        if a1 ==0 or a2 ==0:
            return [min(2,mx),mx]
        mn =left = 0 
        for i,a in enumerate(s):
            while s[left] <=a -n:
                left +=1
            mn = max(mn,i-left +1)
        return [n-mn,mx]

re =Solution().numMovesStonesII([1,100,101,102,103,104])
print(re)