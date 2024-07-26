# https://leetcode.cn/problems/minimum-operations-to-make-array-equal-to-target/description/
# https://leetcode.cn/circle/discuss/nzGQrM/
from typing import List, Tuple, Optional
from itertools import pairwise
class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        ls = [a-b for a,b in zip(nums,target)]
        dls =  [a-b for a,b in pairwise([0] + ls +[0])]
        return sum(a for a in dls if a >0)
