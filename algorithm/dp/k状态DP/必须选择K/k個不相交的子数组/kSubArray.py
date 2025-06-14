# https://leetcode.cn/contest/weekly-contest-388/problems/maximum-strength-of-k-disjoint-subarrays/
# 这里k个数组是不用把所有数组都选择完，所以 dp1[i] = max(dp1[i], dp0[i]) 
# dp0表示未断开的的i个子数组，则由 dp0[i] 和dp1[i-1]转移过来
# 对于新的数字，dp0[i] += (1 if i % 2 else -1) * num * (k - i + 1) 是直接分解得到当前元素的贡献
from typing import List, Tuple, Optional
from math import inf

class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        dp0 = [-inf] * (k + 1)
        dp1 = [-inf] * (k + 1)
        dp0[0] = dp1[0] = 0
        for num in nums:
            # dp0 表示最后一个元素在第 i 个数组中的状态
            # 两种转移过来：前一个位置是否截断
            # dp1 表示该位置第 i 个数组已经截断的情况下的最大价值
            for i in range(k, 0, -1):
                dp0[i] = max(dp0[i], dp1[i-1]) # 因爲 dp1，dp0 初始狀態是 -inf 所以可以直接選擇最大值
                dp0[i] += (1 if i % 2 else -1) * num * (k - i + 1)  ##對與連續的狀態轉移一定是直接加
                dp1[i] = max(dp1[i], dp0[i])  ##對與非連續的狀態轉移
        return dp1[-1]


#作者：小羊肖恩
#链接：https://leetcode.cn/circle/discuss/58wLhi/view/WoV62X/
