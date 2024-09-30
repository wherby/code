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
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)
        dic= defaultdict(set)
        for word in words:
            m = len(word)
            for i in range(1,m+1):
                ret =KMPSearch(word[:i],target)
                for a in ret:
                    dic[a+i].add(i)
                if len(ret) ==0:
                    break
        cnt = 0 
        cand =[n]
        visit ={}
        while cand:
            tmp = set()
            for a in cand:
                if a == 0:
                    return cnt
                if a in visit:
                    continue
                visit[a] = 1
                for b in dic[a]:
                    tmp.add(a-b)
            cnt +=1
            cand = tmp
        return -1



re =Solution().minValidStrings(words = ["abc","aaaaa","bcdef"], target = "aabcdabc")
print(re)