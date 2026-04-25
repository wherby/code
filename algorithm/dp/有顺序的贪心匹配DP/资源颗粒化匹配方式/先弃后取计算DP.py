# dis_sum 看起来没有什么意义，因为不会所有robot都和当前factory 有关联，这里记录这个是为了制造一个相对偏移坐标量
# 在这一步的时候把多减去的相对位移加回去
# # 2. 出
#                 while q[0][0] < j - limit:
#                     q.popleft()

#                 # 3. 队首为滑动窗口最小值
#                 f[j] = dis_sum + q[0][1]
from typing import List, Tuple, Optional
from collections import defaultdict,deque
from math import inf
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        factory.sort(key=lambda f: f[0])
        robot.sort()

        m = len(robot)
        f = [0] + [inf] * m

        for position, limit in factory:
            dis_sum = 0
            q = deque([(0, 0)])
            for j, r in enumerate(robot, 1):  # r = robot[j - 1]
                dis_sum += abs(r - position)

                # 1. 入
                v = f[j] - dis_sum
                while q and q[-1][1] >= v:
                    q.pop()
                q.append((j, v))

                # 2. 出
                while q[0][0] < j - limit:
                    q.popleft()

                # 3. 队首为滑动窗口最小值
                f[j] = dis_sum + q[0][1]

        return f[m]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-total-distance-traveled/solutions/1951947/ji-yi-hua-sou-suo-by-endlesscheng-qctr/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。