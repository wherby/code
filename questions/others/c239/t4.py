import heapq
class Solution(object):
    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        n = len(intervals)
        hp =[]
        hp2 =[]
        m = len(queries)
        res =[-1] *m
        deleted ={}
        for i,x in enumerate(intervals):
            a,b = x
            heapq.heappush(hp,(a,0,b-a+1,i))
            heapq.heappush(hp,(b+0.1,1,0,i))
        for i,q in enumerate(queries):
            heapq.heappush(hp,(q,2,0,i))
        while hp:
            a,cm,d,idx  = heapq.heappop(hp)
            if cm == 0:
                heapq.heappush(hp2,(d,idx))
            if cm ==1:
                deleted[idx] =1
            if cm ==2:
                if len(hp2) == 0:
                    res[i] == -1 
                else:
                    x,id = hp2[0]
                    if id in deleted:
                        heapq.heappop(hp2)
                        heapq.heappush(hp,(a,cm,d,idx))
                    else:
                        res[idx] =x
        #print(deleted,hp2)
        return res

re = Solution().minInterval(intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22])
print(re)
