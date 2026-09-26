

# 矩形上点到圆的最短距离的点
https://leetcode.cn/problems/circle-and-rectangle-overlapping/description/?envType=daily-question&envId=2026-09-19
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        x = max(x1,min(x2,xCenter))
        y = max(y1,min(y2,yCenter))
        return (x-xCenter)**2 + (y-yCenter)**2 <= radius**2 
