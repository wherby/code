# https://leetcode.cn/contest/weekly-contest-319/problems/maximum-number-of-non-overlapping-palindrome-substrings/

from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

def manachers(S):
    A = "@#" + "#".join(S) + "#$"
    Z = [0] * len(A)
    center = right =0
    for i in range(1,len(A)-1):
        if i < right:
            Z[i] = min(right -i,Z[2*center -i])
        while A[i + Z[i]+1] == A[i-Z[i]-1]:
            Z[i] +=1
        if i + Z[i] > right:
            center,right = i , i+ Z[i]
    return Z[2:-2:1]

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        cnt = 0 
        idx = k
        while n >=idx:
            while idx<= n:
                t = s[:idx]
                fd = False
                re = manachers(t)
                print(t,re,s)
                for a in re:
                    if a >= k:
                        fd = True
                        cnt +=1
                        s = s[idx:]
                        idx=k
                        n = len(s)
                if fd ==False:
                    idx +=1
            if idx ==n-1:
                break
        return cnt
                



re =Solution().maxPalindromes(s = "iqqibcecvrbxxj",k=3)
print(re)