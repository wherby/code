# 同余递增
# https://leetcode-cn.com/problems/find-servers-that-handled-most-number-of-requests/
from heapq import heappop, heappush


class Solution(object):
    def busiestServers(self, k, arrival, load):
        """
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        """
        availble = list(range(k))
        busy = []
        ls = [0]*k
        for i, (start,load) in enumerate(zip(arrival,load)):
            while busy and busy[0][0] <= start:
                _,id = heappop(busy)
                heappush(availble,i + (id-i)%k)
            if availble:
                id = heappop(availble) %k
                ls[id] +=1
                heappush(busy,(start+load,id))
        maxR = max(ls)
        return [i for i,a in enumerate(ls) if a ==maxR]
