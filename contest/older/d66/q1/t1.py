from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left
from collections import defaultdict
class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        dic=defaultdict(int)
        dic2 = defaultdict(int)
        for a in words1:
            dic[a] +=1
        for a in words2:
            dic2[a] +=1
        cnt =0 
        keys = list(dic.keys())
        #print(keys,dic,dic2)
        for k in keys:
            if dic[k] ==1 and dic2[k] ==1:
                cnt +=1
        return cnt

re = Solution().countWords(words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"])
print(re)
