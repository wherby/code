from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

def calculate_z_array(s):
    N = len(s)
    Z = [0] * N
    L, R = 0, 0
    for i in range(1, N):
        if i > R:
            L = R = i
            while R < N and s[R - L] == s[R]:
                R += 1
            R -= 1
            Z[i] = R - L + 1
        else:
            k = i - L
            if Z[k] + i <= R:
                Z[i] = Z[k]
            else:
                L = i
                while R < N and s[R - L] == s[R]:
                    R += 1
                R -= 1
                Z[i] = R - L + 1
        #print(i,L,R,Z)
    return Z

class Solution(object):
    def minimumTimeToInitialState(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        n = len(word)
        zf =calculate_z_array(word)
        #print(zf)
        res = (n+k)//k
        for i in range(k,n,k):
            if zf[i] + i ==n:
                return i //k 
            #print(zf[i],k,n,i)
        return res





re =Solution().minimumTimeToInitialState(word = "abacaba", k = 3)
print(re)