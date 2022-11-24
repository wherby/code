# https://leetcode.cn/problems/number-of-subarrays-with-bounded-maximum/
from typing import List, Tuple, Optional
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        lastG,lastB = -1,-1
        cnt=0
        for i,a in enumerate(nums):
            if a > right:
                lastB = i
            elif a >=left:
                lastG = i

            cnt  += max(lastG-lastB,0)
            #print(i,cnt,lastB,lastG)
        return cnt
