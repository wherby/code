# reset 只有在子图所有节点都重置的时候才能使用，单独重置子图的一个节点是没有意义的  ： algorithm/codeforce/图论/节点的边的枚举.py   

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
    
    def reset(self, x: int):
        """
        只有子图所有节点都一起重置才有意义，否则路径压缩过的节点就会出错
        """
        self._fa[x] = x
        self.size[x] = 1