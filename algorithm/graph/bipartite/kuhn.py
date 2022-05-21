#https://cp-algorithms.com/graph/kuhn_maximum_bipartite_matching.html#standard-implementation
class Kuhn:
    def __init__(self,g):
        self.g =g
        self.mt= [-1]*len(g)
        self.used=[False]*len(g)
    
    def try_kuhn(self, v):
        if self.used[v]:
            return False
        self.used[v] = True
        for to in self.g[v]:
            if self.mt[to] == -1 or self.try_kuhn(self.mt[to]):
                self.mt[to] = v 
                return True
        return False
    
    def resove(self):
        n = len(self.g)
        for i in range(n):
            self.used = [False]*n
            self.try_kuhn(i)
        

# algorithm\graph\bipartite\pic\bipartite.drawio.png
# https://app.diagrams.net/#W32d4198629faf020%2F32D4198629FAF020!3354
g =[[],[4,6],[4,5],[4],[1,3],[2],[1]]
k = Kuhn(g)
for i in range(len(g)):
    k.used= [False]*len(g)
    k.try_kuhn(i)
    print(k.mt)

print(k.mt)
k.resove()
print(k.mt)