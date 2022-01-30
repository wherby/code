from collections import defaultdict
class DSU:
    def __init__(self,N):
        self.p  = list(range(N))
        self.rank = [1]*N
    
    def find(self,x):
        if self.p[x] != x:
            self.p[x] =self.find(self.p[x])
        return self.p[x]
    
    def union(self,x,y):
        xr = self.find(x)
        yr = self.find(y)
        if self.rank[xr] <self.rank[yr]:
            xr,yr =yr,xr
        
        self.p[yr] = xr
        if self.rank[xr] == self.rank[yr]:
            self.rank[xr] += 1

class Solution(object):
    def groupStrings(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        dic = {}
        def getV(word):
            t = 0
            for a in word:
                t += 1<<(ord(a)-ord('a'))
            return t
        n = len(words)
        dsu = DSU(n)
        def addToDic(value,idx):
            if value in dic:
                k1 = dic[value]
                dsu.union(k1,idx)
            else:
                dic[value] = idx
        for idx, word in enumerate(words):
            v = getV(word)
            addToDic(v,idx)
            for i in range(26):
                kit = v &(1 <<i)
                j2 = v -kit
                if kit:
                    addToDic(j2,idx)
        dic2=defaultdict(int)
        mx = 0
        for i in range(n):
            k = dsu.find(i)
            dic2[k] +=1
            mx = max(mx,dic2[k])
        return [len(dic2.keys()),mx]


re =Solution().groupStrings(["a","b","ab","cde"])
print(re)