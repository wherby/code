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
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """
        n= len(source)
        dsu= DSU(10**5+2)
        for a,b in allowedSwaps:
            dsu.union(a,b)
        cnt =0
        dic = defaultdict(int)
        dicb = {}
        dic3 = {}
        for a,b in allowedSwaps:
            if a not in dic3:
                dic3[a]= 1
                dicb[source[a]] =a
                dic[source[a]] +=1
            if b not in dic3:
                dic3[b] =1
                dicb[source[b]] =b
                dic[source[b]] +=1
        for i in range(n):
            if source[i] != target[i]:
                a = target[i]
                if dic[a]>0 and dsu.find(i) == dsu.find(dicb[a]) :
                    dic[a] -=1
                else:
                    #print(a,i,dic,dicb[a])
                    cnt +=1
        return cnt

s=[67,71,32,48,71,12,64,20,29,47,90,13,17,94,81,62,24,20,22]
t=[67,6,32,48,36,97,70,29,29,15,90,73,32,94,38,61,24,20,22]
c=[[16,17],[10,4],[6,4],[5,4],[13,15],[7,18],[4,13],[18,12],[14,15],[17,8],[7,11],[18,11],[6,15]]
s=[50,46,54,35,18,42,26,72,75,47,50,4,54,21,18,18,61,64,100,14]
t=[83,34,43,73,61,94,10,68,74,31,54,46,28,60,18,18,4,44,79,92]
c=[[1,8],[14,17],[3,1],[17,10],[18,2],[7,12],[11,3],[1,15],[13,17],[18,19],[0,10],[15,19],[0,15],[6,7],[7,15],[19,4],[7,16],[14,18],[8,10],[17,0],[2,13],[14,10],[12,17],[2,9],[6,15],[16,18],[2,16],[2,6],[4,5],[17,5],[10,13],[7,2],[9,16],[15,5],[0,5],[8,0],[11,12],[9,7],[1,0],[11,17],[4,6],[5,7],[19,12],[3,18],[19,1],[13,18],[19,6],[13,6],[6,1],[4,2]]
re =Solution().minimumHammingDistance(s,t,c)
#re = Solution().minimumHammingDistance([1,5,5],[5,1,1],[[0,1]])
print(re)