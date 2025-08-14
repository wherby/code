# 梯形用斜率和截距分组， 相同斜率的情况下， 不同截距的组合可以构成
# 但是里面会多计算平行四边形的情况， 平行四边形用中点和斜率分组，相同中点的不同斜率的组合能构成平行四边形
from typing import List, Tuple, Optional
from collections import defaultdict,deque
from math import inf
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        cnt = defaultdict(lambda: defaultdict(int))  # 斜率 -> 截距 -> 个数
        cnt2 = defaultdict(lambda: defaultdict(int))  # 中点 -> 斜率 -> 个数

        for i, (x, y) in enumerate(points):
            for x2, y2 in points[:i]:
                dy = y - y2
                dx = x - x2
                if dx == 0:
                    k = inf
                    b = float(x)
                else:
                    k = dy / dx
                    b = (y * dx - dy * x) / dx
                cnt[k][b] += 1  # 按照斜率和截距分组
                cnt2[(x + x2, y + y2)][k] += 1  # 按照中点和斜率分组

        ans = 0
        for ct in cnt.values():
            s = 0
            for c in ct.values():
                ans += s * c
                s += c

        for ct in cnt2.values():
            s = 0
            for c in ct.values():
                ans -= s * c
                s += c

        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/count-number-of-trapezoids-ii/solutions/3728529/tong-ji-zhi-xian-qu-diao-zhong-fu-tong-j-a3f9/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。