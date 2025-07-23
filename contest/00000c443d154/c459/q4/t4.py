from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
from pprint import pprint
INF  = math.inf


def normalize_slope(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    if dx == 0 and dy == 0:
        return (0, 0)
    if dx == 0:
        return (1, 0)  # vertical line
    if dy == 0:
        return (0, 1)  # horizontal line
    g = math.gcd(dy, dx)
    dy //= g
    dx //= g
    if dx < 0:
        dy *= -1
        dx *= -1
    return (dy, dx)

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        dic= defaultdict(list)
        pdic = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            for j in range(i+1,n):
                p1= points[i]
                p2 =points[j]
                slope = normalize_slope(p1,p2)
                dic[slope].append((i,j))
                pdic[i][slope] +=1
                pdic[j][slope] +=1
        cnt = 0 
        print(pdic)
        for slope, edges in dic.items():
            m =len(edges)
            if m < 2:continue
            cnt += m*(m-1)//2
            print(cnt,m,edges)
            for p in pdic:
                c1 = pdic[p][slope]
                if c1 >=2:
                    cnt -= c1*(c1-1) //2
        print(cnt)
        midpoint_dic = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            for j in range(i+1,n):
                p1= points[i]
                p2 = points[j]
                dx = p2[0] - p1[0]
                dy = p2[1] - p1[1]
                midx = (p1[0] +p2[0])/2
                midy = (p1[1] + p2[1])/2
                slope = normalize_slope(p1,p2)
                midpoint_dic[(midx,midy)][slope] +=1
        print(midpoint_dic)
        for mid in midpoint_dic:
            for d in midpoint_dic[mid]:
                c1 = midpoint_dic[mid][d]
                if c1 >=2 :
                    cnt -= c1*(c1-1)//2
        return cnt






re =Solution().countTrapezoids([[82,7],[82,-9],[82,-52],[82,78]])
print(re)