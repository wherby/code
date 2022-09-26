from collections import defaultdict
class Solution(object):
    def transportationHub(self, path):
        """
        :type path: List[List[int]]
        :rtype: int
        """
        ind = defaultdict(int)
        outd = defaultdict(int)
        keys ={}
        for a,b in path:
            ind[b] +=1
            outd[a] +=1
            keys[a]=1
            keys[b]=1
        ret =-1
        m = len(keys.keys())
        for k,v in ind.items():
            if ind[k] ==m-1 and outd[k] ==0:
                return k 
        return ret
            





re =Solution().transportationHub(path = [[0,1],[0,3],[1,3],[2,0],[2,3]])
print(re)