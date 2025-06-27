# https://leetcode.cn/problems/find-maximum-area-of-a-triangle/solutions/3705572/wei-hu-heng-zong-zuo-biao-de-zui-xiao-zh-rhdf/
from typing import List, Tuple, Optional
from collections import defaultdict,deque
# 手写 min max 更快
min = lambda a, b: b if b < a else a
max = lambda a, b: b if b > a else a

class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        ans = 0

        def calc() -> None:
            min_x, max_x = inf, 0
            min_y = defaultdict(lambda: inf)
            max_y = defaultdict(int)
            for x, y in coords:
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                min_y[x] = min(min_y[x], y)
                max_y[x] = max(max_y[x], y)

            nonlocal ans
            for x, y in min_y.items():
                ans = max(ans, (max_y[x] - y) * max(max_x - x, x - min_x))

        calc()

        for p in coords:
            p[0], p[1] = p[1], p[0]
        calc()

        return ans or -1

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/find-maximum-area-of-a-triangle/solutions/3705572/wei-hu-heng-zong-zuo-biao-de-zui-xiao-zh-rhdf/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。