# https://leetcode.cn/problems/find-the-string-with-lcp/
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        ls = [""]*n
        acc = "a"
        for i in range(n):
            if ls[i] =="":
                ls[i] = acc 
                acc = chr(ord(acc)+1)
                if ord(acc)>ord('z')+1:
                    return ""
            for j in range(i,n):
                if lcp[i][j]>0:
                    if ls[j] =="":
                        ls[j] = ls[i]
                    elif ls[j] != ls[i]:
                        return ""
        for i in range(n):
            for j in range(n):
                if ls[i] == ls[j]:
                    if i+1< n and j +1<n:
                        if lcp[i][j] != lcp[i+1][j+1]+1:
                            return ""
                    else:
                        if lcp[i][j] != 1:
                            return ""
                elif lcp[i][j] != 0:
                    return ""
        return "".join(ls)




re =Solution().findTheString(lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]])
print(re)