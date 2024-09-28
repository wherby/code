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
from collections import Counter

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
    
        ls1,ls2 = [0]*26,[0]*26
        for a in word2:
            ls2[ord(a)- ord('a')] +=1
        m = len(set(word2))
        l = 0 
        sm = 0
        acc = 0
        for i,a in enumerate(word1):
            ls1[ord(a)-ord('a')] +=1
            if ls1[ord(a)-ord('a')] == ls2[ord(a)-ord('a')]:
                acc +=1
                #print(acc,i,ls1)
            while acc ==m:
                ls1[ord(word1[l])- ord('a')] -=1
                if ls1[ord(word1[l])- ord('a')] +1 ==ls2[ord(word1[l])- ord('a')]:
                    acc -=1
                l+=1
            sm +=l 
            #print(sm,a,acc)
        return sm





re =Solution().validSubstringCount(word1 = "abcabc", word2 = "aaabc")
print(re)