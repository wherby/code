# 得到重叠的区域直接用 min(tx, tx2) - max(bx, bx2)  # 右上横坐标 - 左下横坐标 这样计算更直接

from typing import List, Tuple, Optional
class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        max_side = 0
        for i, ((bx, by), (tx, ty)) in enumerate(zip(bottomLeft, topRight)):
            if tx - bx <= max_side or ty - by <= max_side:
                continue  # 最优性剪枝：max_side 不可能变大
            for j in range(i):
                bx2, by2 = bottomLeft[j]
                tx2, ty2 = topRight[j]
                width = min(tx, tx2) - max(bx, bx2)  # 右上横坐标 - 左下横坐标
                height = min(ty, ty2) - max(by, by2)  # 右上纵坐标 - 左下纵坐标
                side = min(width, height)
                max_side = max(max_side, side)
        return max_side ** 2


class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        ret = 0 
        n = len(bottomLeft)
        def getOverlap(x1,x2,x3,x4):
            ol = 0 
            if x3<=x1<=x4:
                ol = min(x2,x4) -x1 
            elif x1<=x3<=x2:
                ol = min(x2,x4) -x3 
            return max(ol,0)

        for i in range(n):
            x1,y1 =bottomLeft[i]
            x2,y2 = topRight[i]
            if x2-x1 <= ret or y2-y1<=ret:
                continue
            for j in range(i):
                x3,y3= bottomLeft[j]
                x4,y4 = topRight[j]
                xd = getOverlap(x1,x2,x3,x4)
                yd = getOverlap(y1,y2,y3,y4)
                ret = max(ret,min(yd,xd))
        return ret**2
                    