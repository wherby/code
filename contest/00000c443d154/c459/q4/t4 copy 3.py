from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf


from collections import defaultdict
from math import gcd

MOD = 10**9 + 7

from collections import defaultdict
from math import gcd

MOD = 10**9 + 7

# y = (dy/dx)*x +b
# b = (y*dx-dy*x)/dx

def get_slope(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    if dx == 0 and dy == 0:
        return (0, 0)
    if dx == 0:
        return (1, 0)  # vertical line
    if dy == 0:
        return (0, 1)  # horizontal line
    g = math.gcd(dy, dx)
    dy //= g
    dx //= g
    if dx < 0:
        dy *= -1
        dx *= -1
    return (dy, dx)
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
        for k, ct in cnt.items():
            s = 0
            print(ct.values(),k,ct.keys())
            for c in ct.values():
                ans += s * c
                s += c
                #print(b,cnt,s,k)
        print(cnt)
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


re =Solution().countTrapezoids([[-3,2],[3,0],[2,3],[3,2],[2,-3]])
print(re)