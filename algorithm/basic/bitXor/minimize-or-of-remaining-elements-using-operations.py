# https://leetcode.cn/contest/weekly-contest-382/problems/minimize-or-of-remaining-elements-using-operations/

# 拆位，试填法
# 寻找k段子数组，让mask bit 位合并为0

# 寻找 K 段
# https://leetcode.cn/contest/weekly-contest-382/ranking/

from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(29, -1, -1):
            cur = ans | (1 << i)
            val = -1
            cnt = len(nums)
            for v in nums:
                val &= v & cur
                if val == 0:
                    cnt -= 1
                    val = -1
            if cnt <= k: ans = cur
        return (1 << 30) - 1 - ans




re =Solution().minOrAfterOperations(nums = [37,6,46,32,23],k=3)
re =Solution().minOrAfterOperations([7,3,15,14,2,8] ,4)
print(re)

