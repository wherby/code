# https://www.jb51.net/article/178694.htm <= which not work
#使用atan2函数计算度数，省去了象限的考虑 https://leetcode-cn.com/problems/maximum-number-of-visible-points/solution/python-hua-dong-chuang-kou-gao-qi-easy-to-understa/
import math

def azimuthAngle(x1,y1,x2,y2):
    return math.degrees(math.atan2(y2-y1, x2-x1))

print(azimuthAngle(0,0,1,-1))

