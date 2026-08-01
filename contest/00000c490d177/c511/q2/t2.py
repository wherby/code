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
    def countDominantNodes(self, root: TreeNode | None) -> int:
        cnt = 0 
        
        def dfs(a):
            nonlocal cnt
            if a == None:
                return -1 
            cmx = dfs(a.right)
            cmx = max(cmx,dfs(a.left))
            if cmx <= a.val:
                cnt +=1
            return max(a.val,cmx)
            
        dfs(root)
        return cnt




re =Solution()
print(re)