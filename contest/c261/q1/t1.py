from collections import defaultdict
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt =0
        n= len(s)
        end = -1
        for i in range(n):
            t = s[i]
            if t == "X" and end <=i:
                end = i +3
                cnt +=1
            #print(end)
        return cnt 

re = Solution().minimumMoves("OOOOX22X")
print(re)