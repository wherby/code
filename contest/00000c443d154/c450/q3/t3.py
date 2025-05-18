from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf

class Solution:
    def minMoves(self, mat: List[str]) -> int:
        m,n = len(mat),len(mat[0])
        dic = defaultdict(list)
        cnt = 0
        for i in range(m):
            for j in range(n):
                c = mat[i][j]
                if c !="." and c!="#":
                    dic[c].append((i,j))
        visit = {}
        st = deque([(0,0,0)])
        while st:
            x,y,idx =st.popleft()
            if (x,y) in visit:
                continue
            visit[(x,y)] = idx
            c = mat[x][y]
            if c !="." and c!="#" and c not in visit:
                for x1,y1 in dic[c]:
                    st.appendleft((x1,y1,idx))
                    visit[c] = 1
            for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                if 0<=nx<m and 0<=ny<n and mat[nx][ny] != "#" and (nx,ny) not in visit:
                    st.append((nx,ny,idx+1))
        #print(visit)
        return -1 if (m-1,n-1) not in visit else visit[(m-1,n-1)]





re =Solution().minMoves([".A","CA"])
print(re)