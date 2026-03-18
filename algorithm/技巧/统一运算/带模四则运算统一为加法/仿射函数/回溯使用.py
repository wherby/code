
# https://leetcode.cn/problems/fancy-sequence/description/?envType=daily-question&envId=2026-03-15
# https://leetcode.cn/problems/fancy-sequence/solutions/3917656/lan-geng-xin-deng-jie-zhuan-hua-pythonja-csvl/?envType=daily-question&envId=2026-03-15

mod = 10**9+7
class Fancy:

    def __init__(self):
        self.val = []
        self.add = 0
        self.mul = 1

    def append(self, val: int) -> None:
        self.val.append((val- self.add)*pow(self.mul,-1,mod) %mod)

    def addAll(self, inc: int) -> None:
        self.add += inc
        

    def multAll(self, m: int) -> None:
        self.mul = self.mul * m %mod 
        self.add = self.add * m %mod 

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.val):
            return -1 
        return (self.val[idx]*self.mul + self.add)%mod