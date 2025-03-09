from typing import List, Tuple, Optional

from collections import Counter
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        ans = 1
        for x, c in cnt.items():
            if x - k in cnt:  # x 不是等差数列的首项
                continue
            # 计算这一组的方案数
            f0, f1 = 1, 1 << c
            x += k
            while x in cnt:
                f0, f1 = f1, f1 + f0 * ((1 << cnt[x]) - 1)
                x += k
            ans *= f1  # 每组方案数相乘
        return ans - 1  # 去掉空集

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/the-number-of-beautiful-subsets/solutions/2177818/tao-lu-zi-ji-xing-hui-su-pythonjavacgo-b-fcgs/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。