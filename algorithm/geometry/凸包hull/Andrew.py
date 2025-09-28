
from typing import List, Tuple, Optional
# 计算点集凸包的Andrew算法
def det(x1: int, y1: int, x2: int, y2: int) -> int:
    return x1 * y2 - y1 * x2

def convex_hull(points: List[List[int]]) -> List[List[int]]:
    if len(points) <= 1:
        return points
    
    points.sort()
    
    # 构建下凸包
    lower = []
    for p in points:
        while len(lower) >= 2 and det(lower[-1][0]-lower[-2][0], lower[-1][1]-lower[-2][1], 
                                    p[0]-lower[-1][0], p[1]-lower[-1][1]) <= 0:
            lower.pop()
        lower.append(p)
    
    # 构建上凸包
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and det(upper[-1][0]-upper[-2][0], upper[-1][1]-upper[-2][1], 
                                    p[0]-upper[-1][0], p[1]-upper[-1][1]) <= 0:
            upper.pop()
        upper.append(p)
    
    # 合并结果（去除重复的首尾点）
    return lower[:-1] + upper[:-1]

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        ch = convex_hull(points)

        def area(i: int, j: int, k: int) -> int:
            return det(ch[j][0] - ch[i][0], ch[j][1] - ch[i][1], ch[k][0] - ch[i][0], ch[k][1] - ch[i][1])

        m = len(ch)
        ans = 0
        # 固定三角形的其中一个顶点 ch[i]
        for i in range(m):
            # 同向双指针
            k = i + 2
            for j in range(i + 1, m - 1):
                while k + 1 < m and area(i, j, k) < area(i, j, k + 1):
                    k += 1
                # 循环结束后，ch[k] 距离 ch[i]ch[j] 最远
                ans = max(ans, area(i, j, k))  # 注意这里没有除以 2
        return ans / 2

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/largest-triangle-area/solutions/3793198/liang-chong-fang-fa-mei-ju-tu-bao-xuan-z-1780/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。