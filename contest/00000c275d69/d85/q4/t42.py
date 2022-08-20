import heapq
class DSU:
    def __init__(self,N):
        self.p  = list(range(N))
    def find(self,x):
        if self.p[x] != x:
            self.p[x] =self.find(self.p[x])
        return self.p[x]

    def union(self,x,y):
        self.p[self.find(x)] =self.find(y)


class Solution(object):
    def maximumSegmentSum(self, nums, removeQueries):
        n = len(nums)
        ret = [0]*n 
        st =[0]
        dsu =DSU(n)
        ls = list(nums)
        dic ={}
        
        for i,a in enumerate(reversed(removeQueries)):
            ret[n-1-i] = -st[0]
            if a +1 < n and a+1 in dic:
                x = dsu.find(a+1)
                y = dsu.find(a)
                ls[y] = ls[y]+ ls[x]
                dsu.union(x,y)
            if a -1 >=0 and a-1 in dic:
                x = dsu.find(a-1)
                y = dsu.find(a)
                ls[y] = ls[y]+ ls[x]
                dsu.union(x,y)
            x = dsu.find(a)
            heapq.heappush(st,-ls[x])
            dic[a] =1
        return ret
    
re =Solution().maximumSegmentSum(nums = [1,2,5,6,1], removeQueries = [0,3,2,4,1])
print(re)