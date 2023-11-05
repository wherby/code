import heapq
class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        hp =[]
        hp2 =[]
        idx = 0
        res =[]
        for i,t in enumerate(tasks):
            heapq.heappush(hp,(t[0],t[1],i))
        while hp:
            while hp and hp[0][0]<=idx:
                t = heapq.heappop(hp)
                heapq.heappush(hp2,(t[1],t[2]))
            if not hp2 :
                t = heapq.heappop(hp)
                idx = max(idx + t[1],t[0] + t[1])
                res.append(t[2])
            else:
                t = heapq.heappop(hp2)
                idx += t[0]
                res.append(t[1])
        while hp2:
            t = heapq.heappop(hp2)
            idx += t[0]
            res.append(t[1])
        #print(res)
        return res


tasks = [[1,2],[2,4],[3,2],[4,1]]
re=Solution().getOrder(tasks)
print(re)