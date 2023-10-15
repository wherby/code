# https://leetcode.cn/problems/single-number-ii/description/?envType=daily-question&envId=2023-10-15
from typing import List, Tuple, Optional
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ls =[0]*32
        for a in nums:
            for i in range(32):
                if a &(1<<i):
                    ls[i] +=1
                    ls[i] %=3
        ans = 0
        for i in range(31):
            ans += ls[i]*(1<<i)
        if ls[31]:  # 特殊处理符号位
            ans -= 1<<31
        return ans