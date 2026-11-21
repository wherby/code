from typing import List, Tuple, Optional
from collections import defaultdict, deque


class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        f = defaultdict(int)
        for x in nums:
            f[x + 1] = f[x] + 1
            f[x] = f[x - 1] + 1
        return max(f.values())


# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximize-consecutive-elements-in-an-array-after-modification/solutions/2643723/ben-ti-zui-jian-dan-xie-fa-pythonjavacgo-kcc6/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
