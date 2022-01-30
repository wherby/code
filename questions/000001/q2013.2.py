class DetectSquares:

    def __init__(self):
        self.cnts = defaultdict(lambda:defaultdict(int))

    def add(self, point: List[int]) -> None:
        self.cnts[point[1]][point[0]] += 1

    def count(self, point: List[int]) -> int:
        return sum(v * (self.cnts[(y:=point[1]+diff)][x] * self.cnts[y][point[0]] + self.cnts[(by:=point[1]-diff)][x] * self.cnts[by][point[0]]) for x, v in self.cnts[point[1]].items() if (diff:=x - point[0]) != 0)


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)

作者：himymBen
链接：https://leetcode-cn.com/problems/detect-squares/solution/pythonjavajavascriptgo-ha-xi-tong-ji-mo-uxixs/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。