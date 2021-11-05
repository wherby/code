class Solution(object):
    def canEat(self, candiesCount, queries):
        """
        :type candiesCount: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        n = len(candiesCount)
        ls=[[0,0] for i in range(n)]
        sm =0
        for i,cand in enumerate(candiesCount):
            ls[i][0] = sm
            sm += cand
            ls[i][1] = sm
        m = len(queries)
        res = [False for i in range(m)]
        #print(ls)
        for i,q in enumerate( queries):
            t,d,c = q
            lt = ls[t]
            #print(t,d,c,lt, c * (d+1),(d+1))
            if lt[0] < c * (d+1) and lt[1] >= (d+1):
                res[i]=True
        return res
#candiesCount=[13,45,31,29,13,20,11,33,18,13,10,39,43,36,5,38,27,38,10,33,46,17,20,28,41,29,3,35,38,46,32,7,37,5,27,15,46,9,11,37,47,44,48,34,37,12,3,37,29,25,7,34,45,23,17,10,46,5,37,34,5,45,5]
#queries=[[38,519,36],[62,591,47],[56,137,72],[13,1373,51],[20,355,76],[27,1505,58],[30,1059,16],[44,625,49],[40,1287,27],[5,369,6],[20,307,92],[7,806,42],[33,1672,59],[55,1654,84],[59,730,27],[24,33,63],[27,399,36],[11,1065,10],[39,1649,21],[44,945,49],[56,462,10],[14,341,34],[10,1472,67],[6,1663,91],[15,848,10],[10,742,100],[34,378,49],[25,730,44],[29,847,61],[9,184,58],[59,988,76],[31,1454,13],[21,321,60],[56,914,20],[49,680,26],[41,869,33],[9,1132,59],[3,1200,51],[40,677,56],[1,589,47],[4,1538,29],[37,1489,10],[48,1275,79],[47,793,75],[53,377,13],[27,221,37],[32,1326,45],[38,873,17],[3,630,76],[13,4,91],[18,984,32],[26,1368,23],[59,1151,37],[36,64,82]]
#re=Solution().canEat(candiesCount = [5,2,6,4,1], queries = [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]])
re=Solution().canEat([7,11,5,3,8],[[2,2,6],[4,2,4],[2,13,1000000000]] )
print(re)

#[true,true,true,false,true,false,false,true,false,false,true,false,false,false,true,true,true,false,false,true,true,true,false,false,false,false,true,false,false,true,true,false,true,true,true,true,false,false,true,false,false,false,true,true,true,true,false,true,false,false,false,false,true,true]
#[true,true,true,false,true,false,false,true,false,false,true,false,false,false,true,true,true,false,false,true,true,true,false,false,false,false,true,false,false,true,true,false,true,true,true,true,false,false,true,false,false,false,true,true,true,true,false,true,false,true,false,false,true,true]

