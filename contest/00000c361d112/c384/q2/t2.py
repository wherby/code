from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf
from itertools import pairwise

# https://www.geeksforgeeks.org/python-program-for-kmp-algorithm-for-pattern-searching-2/
# Python program for KMP Algorithm
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
  
    # create lps[] that will hold the longest prefix suffix 
    # values for pattern
    lps = [0]*M
    j = 0 # index for pat[]
  
    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)
    #print(lps)
    res =[]
    i = 0 # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
  
        if j == M:
            #print("Found pattern at index " + str(i-j))
            res.append(i-j)
            j = lps[j-1]
  
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return res
  
def computeLPSArray(pat, M, lps):
    len = 0 # length of the previous longest prefix suffix
  
    lps[0] # lps[0] is always 0
    i = 1
  
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar 
            # to search step.
            if len != 0:
                len = lps[len-1]
  
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1
    #print(lps)
  

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        ret= ""
        for a,b in pairwise(nums):
            if a <b:
                ret +="a"
            elif a== b:
                ret +="b"
            else:
                ret +="c"
        p = ""
        for a in pattern:
            if a ==1:
                p +="a"
            elif a == 0:
                p +="b"
            else:
                p += "c"
        ret = KMPSearch(p,ret)
        return len(ret)





re =Solution().countMatchingSubarrays(nums = [1,4,4,1,3,5,5,3], pattern = [1,0,-1])
print(re)