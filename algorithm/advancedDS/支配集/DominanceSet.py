
from sortedcontainers import SortedList

class DominanceSet:
    def __init__(self):
        # 存储 (x, y)，SortedList 会根据元组第一个元素 x 自动排序
        self.points = SortedList()

    def update(self, x: int, y: int):
        # 1. 寻找插入位置：第一个满足 point.x >= x 的索引
        idx = self.points.bisect_left((x, -float('inf')))
        
        # 2. 支配检查：如果前一个点的得分已经更高，当前点直接废弃
        if idx > 0 and self.points[idx-1][1] >= y:
            return
        
        # 3. 剔除被当前点支配的后续点
        # 注意：这里需要循环删除，直到后方的点 y 值比当前大为止
        while idx < len(self.points) and self.points[idx][1] <= y:
            self.points.pop(idx)
            
        # 4. 插入新点
        self.points.add((x, y))

    def query(self, x: int) -> int:
        # 寻找第一个满足 point.x >= x 的索引
        idx = self.points.bisect_left((x, -float('inf')))
        # 前一个点即为满足 x' < x 且得分最高的点
        if idx > 0:
            return self.points[idx-1][1]
        return 0