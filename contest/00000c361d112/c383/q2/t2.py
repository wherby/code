from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution(object):
    def minimumTimeToInitialState(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        cnt = 1
        word1 =word[k:]+word[:k]
        while word1 != word:
            word1 = word1[k:] + word[:k]
            cnt +=1
            print(word1,word)
        return cnt 





re =Solution().minimumTimeToInitialState(word = "abaabca", k = 3)
print(re)