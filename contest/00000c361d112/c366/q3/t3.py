from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        if (s1.count("1") - s2.count("1"))%2==1:
            return -1
        n = len(s1)
        ls = [i for i in s1]
        cnt =0
        for i in range(n):
            if ls[i] != s2[i]:
                for j in range(1,x+1):
                    if i+j <n:
                        if ls[i+j] !=s2[i+j]:
                            cnt +=j
                            ls[i+j] = s2[i+j]
                            ls[i] = s2[i]
                            #print(ls,cnt)
                            break
        m = 0
        print(ls,cnt)
        for i in range(n):
            if ls[i] != s2[i]:
                m +=1
        return cnt + m//2*x



#re =Solution().minOperations("101101","000000",6)
#print(re ==4)
re =Solution().minOperations("11001011111","01111000110",2)
print(re)