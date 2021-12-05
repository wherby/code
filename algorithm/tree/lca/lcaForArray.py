class LCA:
    def __init__(self,list):
        self.n = len(list)
        self.list =list
        self.parent = [-1]*self.n
        self.level = [-1]*self.n
        self.dic={}
        for i,n in enumerate(list):
            self.dic[n] = i
        self.dfs(0,0,-1)

    def dfs(self,idx,depth,parent):
        if self.list[idx] ==None: return
        self.parent[idx] = parent
        self.level[idx] = depth
        if idx*2+1 <self.n:
            self.dfs(idx*2+1,depth+1,idx)
        if idx*2+2 <self.n:
            self.dfs(idx*2+2,depth +1 ,idx)
    
    def lca(self,a,b):
        a = self.dic[a] # 用index作为计算值
        b = self.dic[b]
        if self.level[a]< self.level[b]:
            a,b = b,a
        while self.level[a] > self.level[b]:
            a =self.parent[a]
        while a !=b:
            a = self.parent[a]
            b = self.parent[b]
        #print(a,b)
        return a
    
    def trace(self,start,end):
        commonAncestor = self.lca(start,end)
        path=[]
        reversPath =[]
        startIdx = self.dic[start]
        endIdx = self.dic[end]
        while startIdx != commonAncestor:
            startIdx = (startIdx-1)//2
            path.append(startIdx)
        while endIdx != commonAncestor:
            endIdx = (endIdx -1) //2
            reversPath.append(endIdx)
        path.extend(reversed(reversPath))
        return path 
    def traceA(self,start,end):
        commonAncestor = self.lca(start,end)
        path=[]
        reversPath =[]
        startIdx = self.dic[start]
        endIdx = self.dic[end]
        while startIdx != commonAncestor:
            startIdx = (startIdx-1)//2
            path.append("U")
        while endIdx != commonAncestor:
            if endIdx %2 ==1:
                reversPath.append("L")
            else:
                reversPath.append("R")
            endIdx = (endIdx -1) //2
        path.extend(reversed(reversPath))
        return path 

root =[7,8,3,1,None,4,5,6,None,None,None,None,None,None,2]
lca = LCA(root)
print(lca.parent)
print(lca.dic)
print(lca.level)
print(lca.lca(7,5))
print(lca.traceA(7,5))