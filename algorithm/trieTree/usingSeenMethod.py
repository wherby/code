# https://leetcode.cn/problems/maximum-strong-pair-xor-ii/description/

from typing import List, Tuple, Optional

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        msk = 0
        for i in range(32,-1,-1):
            msk |=1<<i
            newAns = ans | (1<<i)
            dic = {}
            for a in nums:
                mskA = a &msk 
                if mskA ^ newAns in dic and dic[mskA ^ newAns] *2 >= a :
                    ans = newAns
                    break
                dic[mskA] = a 
        return ans