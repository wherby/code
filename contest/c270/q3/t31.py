class LCA:
    def __init__(self,root):
        self.parent = {}
        self.level = {}
        self.nodeDic ={}
        self.dfs(root,0,-1)
        

    def dfs(self,ele,depth,parent):
        if ele ==None: return
        self.parent[ele.val] = parent
        self.level[ele.val] = depth
        self.nodeDic[ele.val] = ele
        if ele.left:
            self.dfs(ele.left,depth+1,ele.val)
        if ele.right:
            self.dfs(ele.right,depth +1 ,ele.val)
    
    def lca(self,a,b):
        if self.level[a]< self.level[b]:
            a,b = b,a
        while self.level[a] > self.level[b]:
            a =self.parent[a]
        while a !=b:
            a = self.parent[a]
            b = self.parent[b]
        return a
    
    def traceA(self,start,end):
        commonAncestor = self.lca(start,end)
        path=[]
        reversPath =[]
        startIdx = start
        endIdx = end
        while startIdx != commonAncestor:
            startIdx = self.parent[startIdx]
            path.append("U")
        while endIdx != commonAncestor:
            tleft= self.nodeDic[self.parent[endIdx]].left
            if tleft and tleft.val == endIdx:
                reversPath.append("L")
            else:
                reversPath.append("R")
            endIdx = self.parent[endIdx]
        path.extend(reversed(reversPath))
        return path 
class Solution(object):
    def getDirections(self, root, startValue, destValue):
        lca = LCA(root)
        #print(lca.lca(startValue,destValue))
        return "".join(lca.traceA(startValue,destValue))

