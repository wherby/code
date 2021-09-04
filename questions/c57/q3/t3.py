
from queue import PriorityQueue
class Solution(object):
    def splitPainting(self, segments):
        """
        :type segments: List[List[int]]
        :rtype: List[List[int]]
        """
        timeQ= PriorityQueue()
        for seg in segments:
            timeQ.put([seg[0],seg[2],0])
            timeQ.put([seg[1],seg[2],1])
        start = -1
        v =0
        res= []
        while not timeQ.empty():
            re = timeQ.get()
            if re[2] ==0:
                if start == -1:
                    start = re[0]
                    v = re[1]
                else:
                    res.append([start,re[0],v])
                    v = v + re[1]
                    start = re[0]
            else:
                res.append([start,re[0],v])
                v = v-re[1]
                start = re[0]
        res = list(filter(lambda x: x[0] != x[1],res))
        res = list(filter(lambda x: x[2] !=0,res))
        return res



se = [[1,4,5],[1,4,7],[4,7,1],[4,7,11]]
a = Solution().splitPainting(se)
print(a)