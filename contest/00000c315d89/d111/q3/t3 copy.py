from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        dp1, dp2, dp3 = 0, 0, 0
        for num in nums:
            # 这里的 1, 2, 3 实际上指的是下一位可以填的最小数字
            # dp1：下一位是 1，因此只能前面都是 1，只能从 dp1 来，因此如果数 > 1 需要使用 dp1 + 1
            # dp2: 下一位是 2，前面可以是 1 / 2，如果从 1 转移，即前面要求当前位置不小于 1，则只需要把 num 调整到 <= 2 即可；如果前面要求当前位置不小于 2，则这个位置只能是 2
            # dp3：逻辑与 dp2 类似
            dp1, dp2, dp3 = dp1 + (num > 1), min(dp1, dp2 + (num < 2)) + (num > 2), min(dp1, dp2 + (num < 2), dp3 + (num < 3))
        return dp3

#作者：小羊肖恩
#链接：https://leetcode.cn/circle/discuss/s7qlIZ/view/iluIfU/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。




re =Solution().minimumOperations([1,3])
print(re)