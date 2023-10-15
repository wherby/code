from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count("1")<k:
            return ""
        start =0
        cnt =0
        n = len(s)
        ret = ""
        for i in range(n):
            if s[i] == "1":
                cnt +=1
            while cnt > k :
                if s[start] =="1":
                    cnt -=1
                start +=1
            if cnt == k:
                while s[start] =="0":
                    start +=1
                t = s[start:i+1]
                #print(t,cnt,ret,t)
                if ret =="":
                    ret = t 
                elif len(ret)> len(t) or (len(ret) ==len(t) and ret >t):
                    ret =t
        return ret





re =Solution().shortestBeautifulSubstring("1100100101011001001",7)
print(re)

#"1100100101011"
# 1100100101011001001