from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        stLeft, stRight=[],[]
        for i,(l1,p1,l2,p2) in enumerate(time):
            heapq.heappush(stLeft,(-(l1+l2),-i))
        cntRight = 0
        lastTime = 0 
        leftWait,rightWait =[],[]
        leftCnt =0
        while cntRight < n :
            
            while leftWait and leftWait[0][0] <= lastTime:
                a,b,c = heapq.heappop(leftWait)
                heapq.heappush(stLeft,(b,c))
            while rightWait and rightWait[0][0] <= lastTime:
                a,b,c = heapq.heappop(rightWait)
                heapq.heappush(stRight,(b,c))
            if len(stLeft) == len(stRight) == 0:
                if leftWait and rightWait and len(rightWait) + cntRight <n:
                    lastTime = min(leftWait[0][0],rightWait[0][0])
                elif leftWait:
                    lastTime =leftWait[0][0]
                else:
                    lastTime = rightWait[0][0]
            if leftCnt == n and len(stRight) ==0 and len(rightWait)>0:
                lastTime = rightWait[0][0]
            #print(lastTime,stRight,stLeft,leftWait,rightWait,cntRight)
            while leftWait and leftWait[0][0] <= lastTime:
                a,b,c = heapq.heappop(leftWait)
                heapq.heappush(stLeft,(b,c))
            while rightWait and rightWait[0][0] <= lastTime:
                a,b,c = heapq.heappop(rightWait)
                heapq.heappush(stRight,(b,c))
            if stRight:
                b,c = heapq.heappop(stRight)
                cntRight +=1
                lastTime += time[-c][2]
                if leftCnt <n:
                    heapq.heappush(leftWait,(lastTime + time[-c][3],b,c))
            else :
                if leftCnt <n:
                    b,c = heapq.heappop(stLeft)
                    lastTime  += time[-c][0]
                    heapq.heappush(rightWait,(lastTime +time[-c][1],b,c))
                    leftCnt +=1
        return lastTime





#re =Solution().findCrossingTime(n = 3, k = 2, time = [[1,9,1,8],[10,10,10,10]])
#re = Solution().findCrossingTime(10,6,[[2,10,5,8],[3,5,2,2],[5,8,10,10],[7,8,8,5],[5,6,6,10],[6,10,6,2]])
re = Solution().findCrossingTime(9,6,[[2,6,9,4],[4,8,7,5],[4,6,7,6],[2,3,3,7],[9,3,6,8],[2,8,8,4]])
print(re)