# https://cp-algorithms.com/graph/bridge-searching-online.html
# Not verified

class BridgeFind:
    def __init__(self,n) -> None:
        self.par = [0]*n 
        self.dsu_2ecc =[0]*n 
        self.dsu_cc = [0] * n 
        self.dsu_cc_size = [0]*n 
        self.lca_iteration = 0
        self.last_visit = [0]*n 
        for i in range(n):
            self.dsu_2ecc[i] = i
            self.dsu_cc[i] = i 
            self.dsu_cc_size[i] =1 
            self.par[i] = -1
        self.bridges = 0
        
    def find_2ecc(self,v):
        if v == -1:
            return -1
        if self.dsu_2ecc[v] ==v:
            return v
        else:
            self.dsu_2ecc[v] = self.find_2ecc(self.dsu_2ecc[v])
            return self.dsu_2ecc[v]
    
    def find_cc(self,v):
        if v == -1:
            return -1
        if self.dsu_cc[v] == v:
            return v 
        else:
            self.dsu_cc[v] = self.find_cc(self.dsu_cc[v])
            return self.dsu_cc[v]
    
    def make_root(self,v):
        v = self.find_2ecc(v)
        root = v 
        child = -1
        while v !=-1:
            p = self.find_2ecc(self.par[v])
            self.par[v]  = child 
            self.dsu_cc[v] = child
            child = v 
            v = p 
        self.dsu_cc_size[root] = self.dsu_cc_size[child] 
        
    def merge_path(self,a,b):
        self.lca_iteration +=1
        path_a,path_b = [],[]
        lca = -1
        while lca ==-1:
            if a != -1:
                a = self.find_2ecc(a)
                path_a.append(a)
                if self.last_visit[a] == self.lca_iteration:
                    lca = a 
                    break
                self.last_visit[a] = self.lca_iteration
                a = self.par[a]
            if b != -1:
                b = self.find_2ecc(b)
                path_b.append(b)
                if self.last_visit[b] == self.lca_iteration:
                    lca = b 
                    break
                self.last_visit[b] = self.lca_iteration
                b = self.par[b]
        for v in path_a:
            self.dsu_2ecc[v] = lca
            if v == lca:
                break
            self.bridges -=1
        for v in path_b:
            self.dsu_2ecc[v] = lca
            if v == lca:
                break
            self.bridges -=1
    
    def add_edge(self, a, b):
        a = self.find_2ecc(a)
        b = self.find_2ecc(b)
        if a ==b :
            return
        
        ca = self.find_cc(a)
        cb = self.find_cc(b) 
        
        if ca != cb:
            self.bridges +=1
            if self.dsu_cc_size[ca] > self.dsu_cc_size[cb]:
                a,b = b,a 
                ca,cb = cb,ca 
            self.make_root(a)
            self.par[a] = self.dsu_cc[b]  = b 
            self.dsu_cc_size[cb] += self.dsu_cc_size[a] 
        else:
            self.merge_path(a,b)
            
            
bf = BridgeFind(6)
bf.add_edge(0,1)
print(bf.bridges)
bf.add_edge(1,2)
print(bf.bridges)
bf.add_edge(2,3)
print(bf.bridges)
bf.add_edge(3,4)
print(bf.bridges)
bf.add_edge(4,5)
print(bf.bridges)
bf.add_edge(0,3)
print(bf.bridges)
bf.add_edge(0,4)
print(bf.bridges)
