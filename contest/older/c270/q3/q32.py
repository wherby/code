
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
class Solution(object):
    def getDirections(self, root, startValue, destValue):
        lca = LCA(root)
        return "".join(lca.traceA(startValue,destValue))



root =[7,8,3,1,None,4,5,6,None,None,None,None,None,None,2]
lca = LCA(root)
print(lca.parent)
print(lca.dic)
print(lca.level)
print(lca.lca(7,5))
print(lca.traceA(7,5))

# [152,87,237,263,153,27,282,163,37,243,null,128,143,242,5,50,6,166,131,157,null,106,24,147,304,209,148,279,95,311,null,null,null,120,251,null,125,null,122,70,252,182,219,null,160,254,205,41,240,78,267,88,303,57,262,null,null,null,null,179,null,null,null,null,null,33,60,2,76,155,94,265,191,null,null,44,307,null,null,258,null,66,38,20,109,293,61,275,19,58,65,151,72,null,132,null,108,228,225,207,189,null,null,138,54,290,249,170,264,102,140,187,null,46,92,172,null,40,null,null,16,248,null,81,17,233,null,83,null,null,100,null,103,7,175,256,130,235,127,159,10,288,113,99,11,null,null,105,123,23,223,96,192,55,154,97,85,8,126,null,68,4,277,142,230,null,null,null,199,145,86,239,133,306,null,null,null,null,150,null,176,null,null,244,null,null,null,null,null,222,null,null,197,89,null,71,null,null,null,null,115,null,null,null,284,32,289,134,180,124,253,35,261,276,309,136,271,9,null,null,null,144,101,14,null,null,null,null,193,257,186,266,285,null,137,139,59,null,null,229,302,null,107,null,281,18,245,177,185,null,216,114,null,255,174,null,null,1,null,null,null,null,null,null,null,null,214,null,121,259,null,null,null,null,null,null,null,null,null,null,39,null,null,null,null,73,231,53,null,null,51,296,null,117,90,31,215,238,80,null,null,null,194,299,146,null,212,null,null,null,null,67,104,135,null,null,null,null,null,232,280,42,null,null,null,82,278,null,218,28,29,null,null,null,null,34,270,297,173,274,247,null,null,null,null,null,204,null,null,77,null,null,246,null,null,null,null,null,null,null,null,52,null,null,null,null,169,null,null,110,null,312,null,null,null,null,null,167,162,184,272,149,300,234,null,217,79,308,116,null,null,null,null,null,null,62,43,310,null,null,null,220,260,null,48,203,null,null,null,null,null,93,null,null,null,null,null,null,null,null,null,null,null,null,null,null,195,null,158,null,null,250,null,null,241,null,null,null,null,111,15,null,3,63,49,210,313,292,171,168,47,269,141,211,null,56,null,null,null,45,200,null,null,286,null,221,null,null,36,null,null,75,198,188,null,301,null,null,null,null,null,null,64,null,null,null,null,null,null,null,null,null,165,287,null,null,null,224,null,null,null,295,null,null,112,null,null,227,null,null,null,null,null,305,196,null,null,null,null,null,null,22,213,208,202,null,null,236,181,null,null,null,null,null,null,null,null,null,null,null,null,98,null,null,156,null,null,268,164,161,null,273,null,null,null,null,21,null,226,178,298,null,291,null,null,null,91,null,294,null,null,12,null,null,null,183,null,null,null,118,null,null,null,null,null,129,null,13,119,null,null,null,null,null,null,null,283,null,null,null,null,null,null,201,null,314,84,null,null,null,null,null,null,26,74,190,69,206,null,null,null,null,null,30,25]
# 51
# 259
re = Solution().getDirections(root =[7,8,3,1,None,4,5,6,None,None,None,None,None,None,2], startValue = 7, destValue = 5)
print(re)