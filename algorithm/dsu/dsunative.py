#this will record "father order" which tarjan needs 
# Only this way will works for ../tree/lca/tarjan.py
class DSU:
    def __init__(self,N):
        self.p  = list(range(N))
        self.rank = [1]*N
    
    def find(self,x):
        if self.p[x] != x:
            self.p[x] =self.find(self.p[x])
        return self.p[x]
    
    def union(self,x,y):
        self.p[y]= x