from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        cnt = 0
        st =[root]
        while len(st) > 0:
            tmp =[]
            ls =[]
            for a in st:
                if a.left:
                    tmp.append(a.left)
                if a.right:
                    tmp.append(a.right)
                ls.append(a.val)
            st = tmp 
            kls = list(ls)
            kls.sort()
            dic = {}
            cc = 0
            for i,a in enumerate(ls):
                dic[a] = i
            visit={}
            for i,a in enumerate(kls):
                visit[a] =1
                if a != kls[i]:
                    cur = i 
                    while ls[cur]!=a:
                        cur = kls[]
        return cnt

## [332,463,103,417,150,409,41,135,129,117,474,263,null,328,456,347,167,383,null,null,422,493,489,275,72,null,null,425,89,null,null,162,18,null,null,null,null,363,290,106,260,468,null,null,null,432,null,323,null,null,null,null,null,null,36,null,null,302,190,null,280,null,null,null,null,488,null,null,null,null,446,null,null,null,null,null,75]
## 24




re =Solution()
print(re)