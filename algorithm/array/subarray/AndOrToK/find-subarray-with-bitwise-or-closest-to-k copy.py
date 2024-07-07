# find-subarray-with-bitwise-or-closest-to-k
# https://leetcode.cn/problems/find-subarray-with-bitwise-or-closest-to-k/solutions/2798206/li-yong-and-de-xing-zhi-pythonjavacgo-by-gg4d/

# 求子数组and和与k最近的值
from typing import List, Tuple, Optional
from math import inf
from collections import defaultdict,deque
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        pre= defaultdict(int)
        ans = inf
        for i, x in enumerate(nums):
            ans = min(ans, abs(x - k))
            cur = defaultdict(int)
            cur[x]=1
            for key in pre.keys():
                cur[key|x] =1
                ans =min(ans, abs((key|x) - k))
            pre= cur
        return ans

re =Solution().minimumDifference([1,8],10)
print(re)