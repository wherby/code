# 分组计算，递推，乘法原理
from typing import List, Tuple, Optional
from collections import defaultdict,deque
from collections import Counter

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        groups = defaultdict(Counter)
        for x in nums:
            # 模 k 同余的数分到同一组，记录元素 x 及其出现次数
            groups[x % k][x] += 1

        ans = 1
        for cnt in groups.values():
            # 计算这一组的方案数
            a = sorted(cnt.items())
            m = len(a)
            f = [0] * (m + 1)
            f[0] = 1
            f[1] = 1 << a[0][1]
            for i in range(1, m):
                if a[i][0] - a[i - 1][0] == k:
                    f[i + 1] = f[i] + f[i - 1] * ((1 << a[i][1]) - 1)
                else:
                    f[i + 1] = f[i] << a[i][1]
            ans *= f[m]  # 每组方案数相乘
        return ans - 1  # 去掉空集


# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/the-number-of-beautiful-subsets/solutions/2177818/tao-lu-zi-ji-xing-hui-su-pythonjavacgo-b-fcgs/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。