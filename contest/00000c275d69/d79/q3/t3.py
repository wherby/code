from re import L


class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        inord =[0]*n
        for a,b in roads:
            inord[a]+=1
            inord[b]+=1
        inord.sort()
        ret =0
        for i in range(1,n+1):
            ret += i * inord[i-1]
        return ret
    
re =Solution().maximumImportance(n = 5, roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]])
print(re)