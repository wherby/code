from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left
from functools import cache

class Solution:
    def countTime(self, time: str) -> int:
        time = time[:2] + time[3:]
        print(time)
        cnt =0 
        ls =[[] for _ in range(4)]
        for i in range(4):
            if time[i] == "?":
                ls[i].extend([j for j in range(10)])
            else:
                ls[i].append(int(time[i]))
        for i in ls[0]:
            for j in ls[1]:
                for k in ls[2]:
                    for m in ls[3]:
                        if i*10+j <24 and k*10+m <60:
                            cnt +=1
        return cnt
        





re =Solution().countTime("0?:0?")
print(re)