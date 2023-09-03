from typing import List, Tuple, Optional
# https://leetcode.cn/circle/discuss/ZzhMI6/
from collections import Counter

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        c= Counter([0])
        acc = 0
        cur = 0
        for a in nums:
            cur += a%modulo == k 
            cur = cur%modulo
            acc += c[(cur-k) %modulo]
            c[cur]+=1
            #print(c)
        return acc





re =Solution().countInterestingSubarrays(nums = [4,5], modulo = 1, k = 0)
print(re)