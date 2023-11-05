from collections import defaultdict
import collections
import math
class DetectSquares:

    def __init__(self):
        self.pst =[]
        self.pstCount = defaultdict(int)
        

    def add(self, point) -> None:
        self.pst.append(point)
        self.pstCount[(point[0],point[1])] +=1
            

    def count(self, point) -> int:
        px,py =point
        cnt =0
        for x,y in self.pst:
            if px ==x or py == y or abs(x-px) != abs(y-py):
                continue
            cnt += self.pstCount[(px,y)] * self.pstCount[(x,py)]
        return cnt