# 逆时针排序的凸包

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
    
    Args:
        points: 包含 (x, y) 元组的列表。
        
    Returns:
        包含凸包顶点的列表，按逆时针顺序排列。
    """
    n = len(points)
    if n <= 3:
        # 如果点少于等于3个，所有点都在凸包上
        return points

    # 1. 找到 y 坐标最小的点作为基准点
    # 如果 y 相同，选择 x 最小的
    start_point = min(points, key=lambda p: (p[1], p[0]))
    
    # 2. 按极角对其他点排序
    # 这里使用 atan2 而不是叉积，更简单直观
    sorted_points = sorted(points, key=lambda p: math.atan2(p[1] - start_point[1], p[0] - start_point[0]))

    # 3. 遍历并构建凸包
    hull = []
    # 初始将前两个点添加到栈中
    hull.append(sorted_points[0])
    hull.append(sorted_points[1])
    
    for i in range(2, n):
        # 持续检查并移除凹陷点
        while len(hull) >= 2 and check(hull[-2], hull[-1], sorted_points[i]) <= 0:
            hull.pop()
        hull.append(sorted_points[i])
    return hull