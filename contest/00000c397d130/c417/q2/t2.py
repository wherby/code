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

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowls=set(['a', 'e', 'i', 'o',  'u'])
        c = defaultdict(int)
        l = 0
        ret = 0

        for i,a in enumerate(word):
            if a in vowls:
                c[a]+=1
            else:
                c["b"] +=1
            #print(i,l,c)

            while c["b"]>k:
                if word[l] in vowls:
                    c[word[l]] -=1
                else:
                    c["b"] -=1
                l +=1
            if c["b"] ==k and all(c[a] >0 for a in vowls):
                while word[l] in vowls and all(c[a] >0 for a in vowls):
                    c[word[l]] -=1
                    l +=1

                for j in range(l,-1,-1):
                    if word[j] in vowls:
                        ret +=1
                    else:
                        break
                
        return ret




#re =Solution().countOfSubstrings(word = "aeiou", k = 0)
#re =Solution().countOfSubstrings(word = "ieaouqqieaouqq", k = 1) #3
re =Solution().countOfSubstrings(word = "iqeaouqi", k = 2) # 2

#re =Solution().countOfSubstrings(word = "eioaua", k = 0) #2
print(re)