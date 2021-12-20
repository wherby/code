import math
from bisect import bisect_right
def azimuthAngle(x1,y1,x2,y2):
    return math.degrees(math.atan2(y2-y1, x2-x1))

class Solution:
    def visiblePoints(self, points: list[list[int]], angle: int, location: list[int]) -> int:
        n = len(points)
        angles = []
        p1 = location
        samePoint =0
        for i,p2 in enumerate(points):
            if p1[0] == p2[0] and p1[1] == p2[1]:
                samePoint +=1
            else: 
                t = math.degrees(math.atan2(p2[1]-p1[1],p2[0]-p1[0]))
                #print(p1[0],p1[1],p2[0],p2[1])
                angles.append(t)
        #print(angles)
        angles.sort()
        extendAngel = [0]*2 * len(angles)
        for i,a in enumerate(angles):
            extendAngel[i] = a
            extendAngel[i+len(angles)] = a + 360
        mx =0
        for i in range(len(angles)):
            t = extendAngel[i]
            idx = bisect_right(extendAngel,t+angle)
            mx = max(mx, idx-i)
            mx = min(mx, len(angles))
        #print(extendAngel)
        return mx +samePoint