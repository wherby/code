from collections import defaultdict
class Solution:
    def gridIllumination(self, n, lamps, queries):
        """
        :type n: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        m = len(queries)
        res =[0]*m
        dicx =defaultdict(int)
        dicy = defaultdict(int)
        dicxy = defaultdict(int)
        dicxpy = defaultdict(int)
        dicxmy = defaultdict(int)
        for x,y in lamps :
            if dicxy[(x,y)] ==0:
                dicx[x] +=1
                dicy[y] +=1
                dicxy[(x,y)] =1
                dicxpy[x+y] +=1
                dicxmy[x-y] +=1
        arrs = [[1,0],[0,0],[-1,0],[1,1],[0,1],[-1,1],[1,-1],[0,-1],[-1,-1]]
        for i,q in enumerate(queries):
            x,y = q
            if dicx[x] >0 or dicy[y] >0 or dicxpy[x+y] >0 or dicxmy[x-y] >0:
                res[i]=1
            for a,b in arrs:
                x1 ,y1 = x +a,y +b
                if x1 >=0 and x1 < n and y1 >=0 and y1 <n and dicxy[(x1,y1)] >0 :
                    dicx[x1] -=1
                    dicy[y1] -=1
                    dicxy[(x1,y1)] =0
                    dicxpy[x1+y1] -=1
                    dicxmy[x1-y1] -=1
        return res

re = Solution().gridIllumination(n = 6, lamps = [[2,5],[4,2],[0,3],[0,5],[1,4],[4,2],[3,3],[1,0]], queries = [[4,3],[3,1],[5,3],[0,5],[4,4],[3,3]])
print(re)
