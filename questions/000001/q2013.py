from collections import defaultdict
class DetectSquares:

    def __init__(self):
        self.dicx = defaultdict(list)
        self.dic3 = defaultdict(int)
        self.dic2 ={}


    def add(self, point: List[int]) -> None:
        x,y = point
        if (x,y) not in self.dic2:
            self.dic2[(x,y)] =1
            self.dicx[x].append([x,y])
        self.dic3[(x,y)] +=1


    def count(self, point: List[int]) -> int:
        x1,y1 = point
        sm=0
        for x1,y2 in self.dicx[x1]:
            if y1 != y2:
                d = y1-y2
                x3 = x1 +d
                x4 = x1 -d
                sm += self.dic3[(x3,y1)] * self.dic3[(x3,y2)] * self.dic3[(x1,y2)]
                sm += self.dic3[(x4,y1)] * self.dic3[(x4,y2)] * self.dic3[(x1,y2)]
        return sm


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point) 