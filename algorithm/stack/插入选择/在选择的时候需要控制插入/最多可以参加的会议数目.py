# 左边界插入，用右边界选择，在选择的同时改变了左边界的值，所以需要再插入
from typing import List, Tuple, Optional
from heapq import heapify,heappop,heappush 
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        cur =0
        st = []
        n = len(events)
        i  = 0
        cnt = 0
        while i < n:
            cur = max(cur,events[i][0])
            heappush(st,events[i][1])
            #print(st,cur)
            i+=1
            while i < n and events[i][0]<= cur:
                heappush(st,events[i][1])
                i+=1
            while st:
                a = heappop(st)
                if a <cur:
                    continue
                else:
                    cur +=1
                    cnt +=1
                    while i < n and events[i][0]<= cur:
                        heappush(st,events[i][1])
                        i+=1
                #print(cnt,a,cur,st)
        return cnt 

re = Solution().maxEvents([[1,2],[1,2],[3,3],[1,5],[1,5]])
print(re)