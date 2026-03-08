

class UnionFind:
    def __init__(self, n: int):
        self._fa = list(range(n))  
        self.cc = n  
        self.n = n 
        self.size = [1] * n 

    def init(self):
        self.cc = self.n 
        self._fa = list(range(self.n)) 
        self.size = [1] * self.n

    def getSize(self, x: int) -> int:
        return self.size[self.find(x)]  

    def find(self, x: int) -> int:
        if self._fa[x] != x:
            self._fa[x] = self.find(self._fa[x]) 
        return self._fa[x]

    def merge(self, from_: int, to: int) -> bool:
        x, y = self.find(from_), self.find(to)
        if x == y:  
            return False
        self._fa[x] = y 
        self.size[y] += self.size[x]  
        self.cc -= 1 
        return True