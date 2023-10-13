from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        n = len(s1)
        diffs = []
        for i in range(n):
            if s1[i] != s2[i]:
                diffs.append(i)
        m = len(diffs)
        if m %2==1:
            return -1
        @cache
        def dp(l,r):
            if  l>r:
                return 0
            #print(l,r)
            a1 = diffs[r] -diffs[l] if diffs[r] -diffs[l] <=x else x
            a2 = diffs[l+1] - diffs[l] if diffs[l+1] - diffs[l] <= x else x
            a3 = diffs[r] -diffs[r-1] if diffs[r] -diffs[r-1] <=x else x
            #print(a1,a2)
            return min( dp(l+2,r) +a2, dp(l+1,r-1)+a1, dp(l,r-2)+a3)
        #print(m)
        return dp(0,m-1)




#re =Solution().minOperations("101101","000000",6)
#print(re)
re =Solution().minOperations("100010010100111100001110101111100001001101011010100111101011100100011111110001011001001","000001100010010011111101100101111011101110010001001010100101011100011110000111010011010",6)
print(re)