# find-subarray-with-bitwise-or-closest-to-k
# https://leetcode.cn/problems/find-subarray-with-bitwise-or-closest-to-k/submissions/571105794/?envType=daily-question&envId=2024-10-09

# 求子数组and和与k最近的值
from typing import List, Tuple, Optional
from math import inf
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        dic ={}

        ret = 10**40
        for a in nums:
            tmp = {}
            tmp[a] =1 
            ret = min(ret, abs(a-k))
            for b in dic:
                c = b|a 
                tmp[c] = 1
                ret = min(ret,abs(c -k) )
            dic = tmp 
        return ret