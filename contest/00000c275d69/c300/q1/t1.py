from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dic = {}
        idx =0
        for a in key:
            if a not in dic and a.isalpha():
                dic[a] = chr(ord('a')+idx)
                idx +=1
        ret = ""
       # print(dic)
        for a in message:
            if a.isalpha():
                ret += dic[a]
            else:
                ret += a 
        return ret




re =Solution().decodeMessage(key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv")
print(re)