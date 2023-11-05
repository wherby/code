from collections import defaultdict
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        dic =defaultdict(list)
        for i,a in enumerate(arr):
            dic[a].append(i)
        res=[]
        print(dic)
        for a,v in dic.items():
            if len(v) ==1:
                res.append((v[0],a))
        if len(res)< k:
            return ""
        res = sorted(res)
        return res[k-1][1]

arr = ["d","b","c","b","c","a"]
k = 2
re=Solution().kthDistinct(arr,k)
print(re)