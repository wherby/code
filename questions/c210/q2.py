class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        ls = [0]*n
        dic ={}
        for road in roads:
            a,b =road
            a,b = max(a,b),min(a,b)
            ls[a] +=1
            ls[b] +=1
            dic[(a,b)] =1
        mx = 0
        for a in range(n):
            for b in range(a+1,n):
                t = ls[a]+ls[b]
                if t >mx:
                    if (b,a) in dic:
                        mx = max(mx, t-1)
                    else:
                        mx = max(mx,t)
        #print(ls)
        return mx
        
re=Solution().maximalNetworkRank(8,[[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]])
print(re)