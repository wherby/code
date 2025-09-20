
import math

# y = (dy/dx)*x +b
# b = (y*dx-dy*x)/dx
# b 表示 直线与y轴相交的交点， 如果dx ==0 ，直线与y 轴不相交，这时候可以把交点记录为与x轴相交，做了这个运算得到的值，需要与斜率一起记录才能有意义

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

def getBPoint(p1,p2):
    x1,y1 = p1 
    x2,y2 = p2 
    dy,dx = get_slope(p1,p2)
    if dx ==0:
        b = x1 
    else:
        b = (y1 * dx - x1*dy) /dx 
    return (dy,dx, b)
