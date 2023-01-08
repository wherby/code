from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
from collections import Counter
class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        c1,c2 = Counter(word1),Counter(word2)
        small_letters = list(map(chr, range(ord('a'), ord('z')+1)))
        #print(small_letters)
        for a in small_letters:
            for b in small_letters:
                #print(a,b,c1,c2)
                if c1[a] >0 and c2[b] >0:
                    c1[b] +=1
                    c2[a] +=1
                    c1[a] -=1
                    c2[b] -=1
                    #print(c1,c2,a,b)
                    if len([v for v in c1.values() if v >0]) == len([v for v in c2.values() if v >0]):
                        return True
                    c1[b] -=1
                    c2[a] -=1
                    c1[a] +=1
                    c2[b] +=1
        return False
                





re =Solution().isItPossible(word1 = "abcc", word2 = "aab")
print(re)