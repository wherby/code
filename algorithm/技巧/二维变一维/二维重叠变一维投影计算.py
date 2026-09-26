# https://leetcode.cn/problems/rectangle-overlap/description/?envType=daily-question&envId=2026-09-14
# 矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。矩形的上下边平行于 x 轴，左右边平行于 y 轴。
# 如果相交的面积为 正 ，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。
# 给出两个矩形 rec1 和 rec2 。如果它们重叠，返回 true；否则，返回 false 。

# 重叠的时候的判定 max(s1,s2)<min(e1,e2)


from typing import List, Tuple, Optional

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        def isOverlap(s1,e1,s2,e2):
            return max(s1,s2)<min(e1,e2)
        return isOverlap(rec1[0],rec1[2],rec2[0],rec2[2]) and isOverlap(rec1[1],rec1[3],rec2[1],rec2[3])
    

# class Solution:
#     def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
#         def isOverlap(s1,e1,s2,e2):
#             if s1 >s2:
#                 s1,e1,s2,e2 = s2,e2,s1,e1 
#             return s2<e1
#         return isOverlap(rec1[0],rec1[2],rec2[0],rec2[2]) and isOverlap(rec1[1],rec1[3],rec2[1],rec2[3])