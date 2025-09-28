
import math

def check(p1, p2, p3):
    """
    判断三个点 p1, p2, p3 的方向。
    返回正值表示逆时针，负值表示顺时针，0 表示共线。
    """
    val = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    if val == 0:
        return 0  # 共线
    return 1 if val > 0 else -1  # 逆时针或顺时针

def convex_hull(points):
    """
    使用 Graham Scan 算法计算二维点集的凸包。
    """
    n = len(points)
    if n <= 3:
        return points

    # 1. 找到 y 坐标最小的点作为基准点
    start_point = min(points, key=lambda p: (p[1], p[0]))
    
    # 2. 按极角排序（使用叉积而不是 atan2）
    def polar_angle(p):
        # 计算相对于基准点的极角
        dx = p[0] - start_point[0]
        dy = p[1] - start_point[1]
        return math.atan2(dy, dx)  # 暂时保留，后面会优化
    
    # 更好的排序函数：使用叉积
    def compare(p1, p2):
        if p1 == start_point:
            return -1
        if p2 == start_point:
            return 1
            
        # 计算叉积
        cross = (p1[0] - start_point[0]) * (p2[1] - start_point[1]) - (p1[1] - start_point[1]) * (p2[0] - start_point[0])
        
        if cross == 0:
            # 共线时，距离基准点近的排在前面
            dist1 = (p1[0] - start_point[0])**2 + (p1[1] - start_point[1])**2
            dist2 = (p2[0] - start_point[0])**2 + (p2[1] - start_point[1])**2
            return -1 if dist1 < dist2 else 1
        return -1 if cross > 0 else 1

    # 排序点集（排除基准点）
    other_points = [p for p in points if p != start_point]
    sorted_points = sorted(other_points, key=lambda p: (
        math.atan2(p[1]-start_point[1], p[0]-start_point[0]),
        (p[0]-start_point[0])**2 + (p[1]-start_point[1])**2
    ))
    
    # 将基准点放在开头
    sorted_points = [start_point] + sorted_points

    # 3. 构建凸包
    hull = []
    hull.append(sorted_points[0])
    hull.append(sorted_points[1])
    
    for i in range(2, len(sorted_points)):
        while len(hull) >= 2 and check(hull[-2], hull[-1], sorted_points[i]) != 1:
            hull.pop()
        hull.append(sorted_points[i])
    
    return hull

from typing import List, Tuple, Optional
# 计算点集凸包的Andrew算法
def det(x1: int, y1: int, x2: int, y2: int) -> int:
    return x1 * y2 - y1 * x2


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
                ans = max(ans,abs(area(i, j, k)))  # 注意这里没有除以 2
        return ans / 2

re = Solution().largestTriangleArea([[1,0],[0,0],[0,1]])
print(re)