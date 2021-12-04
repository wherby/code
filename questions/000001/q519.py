import random
class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.map = {}

    def flip(self):
        x = 0#random.randint(0, self.total - 1)
        print(self.map)
        self.total -= 1
        # 查找位置 x 对应的映射
        idx = self.map.get(x, x)
        print(self.map)
        # 将位置 x 对应的映射设置为位置 total 对应的映射
        self.map[x] = self.map.get(self.total, self.total)
        print(self.map,idx,self.total,x)
        return [idx // self.n, idx % self.n]
        
    def reset(self) -> None:
        self.total = self.m * self.n
        self.map.clear()

re =Solution(3,1)
print(re.flip())
print(re.flip())
print(re.flip())
print(re.map)

