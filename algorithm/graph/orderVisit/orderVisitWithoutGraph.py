#https://leetcode.cn/contest/weekly-contest-308/problems/build-a-matrix-with-conditions/

from collections import defaultdict,deque

def ordVisitWithOutGraph(condition,keys=None):
    g = defaultdict(list)
    ind =defaultdict(int)
    for a,b in condition:
        g[a-1].append(b-1) ## start from 1 need handle
        ind[b-1] +=1
    st =deque([])
    if keys ==None:
        keys= list(g.keys())
    for k in keys:
        if ind[k] == 0:
            st.append(k)
    ret =[]
    while st:
        b= st.popleft()
        ret.append(b)
        for c in g[b]:
            ind[c] -=1
            if ind[c] ==0:
                st.append(c)
    return ret


class Solution(object):
    def buildMatrix(self, k, rowConditions, colConditions):
        """
        :type k: int
        :type rowConditions: List[List[int]]
        :type colConditions: List[List[int]]
        :rtype: List[List[int]]
        """
        keys = [i for i in range(k)]
        rret,cret =ordVisitWithOutGraph(rowConditions,keys),ordVisitWithOutGraph(colConditions,keys)
        rdic,cdic ={},{}
        for i,a in enumerate(rret):
            rdic[a+1] = i 
        for i,a in enumerate(cret):
            cdic[a+1] =i  
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