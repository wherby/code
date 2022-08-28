from collections import defaultdict,deque
class Solution(object):
    def buildMatrix(self, k, rowConditions, colConditions):
        """
        :type k: int
        :type rowConditions: List[List[int]]
        :type colConditions: List[List[int]]
        :rtype: List[List[int]]
        """
        gr,gc =[[] for _ in range(k)],[[] for _ in range(k)]
        indR,indC =[0]*k,[0]*k
        for a,b in rowConditions:
            gr[b-1].append(a-1)
            indR[a-1]+=1
        for a,b in colConditions:
            gc[b-1].append(a-1)
            indC[a-1] +=1
        def findOrd(gr,ord):
            ret= []
            acc =0
            seed =deque([])
            for i,a in enumerate(ord):
                if a ==0:
                    seed.append(i)
            while seed:
                b =  seed.popleft()
                ret.append(b)
                acc +=1
                for c in gr[b]:
                    ord[c] -=1
                    if ord[c] ==0:
                        seed.append(c)
            return ret
        rret,cret = findOrd(gr,indR),findOrd(gc,indC)
        rdic,cdic ={},{}
        for i,a in enumerate(rret):
            rdic[a+1] = k-1-i 
        for i,a in enumerate(cret):
            cdic[a+1] =k-1-i  
        if len(rret) ==k and len(cret) ==k:
            res = [[0]*k for _ in range(k)]
            for i in range(1,k+1):
                res[rdic[i]][cdic[i]] =i
            return res
        else:
            return []



k=8
rowConditions=[[1,2],[7,3],[4,3],[5,8],[7,8],[8,2],[5,8],[3,2],[1,3],[7,6],[4,3],[7,4],[4,8],[7,3],[7,5]]
colConditions=[[5,7],[2,7],[4,3],[6,7],[4,3],[2,3],[6,2]]
re =Solution().buildMatrix(k , rowConditions, colConditions )
#re =Solution().buildMatrix(k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]])
print(re)