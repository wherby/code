class Solution(object):
    def edgeScore(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        n =len(edges)
        ls = [0]*n
        for i,a in enumerate(edges):
            ls[a] += i 
        mx =0
        idx =0
        for i in range(n):
            if ls[i]>mx:
                mx = ls[i]
                idx = i
        return idx



re =Solution().edgeScore( [1,0,0,0,0,7,7,5])
print(re)