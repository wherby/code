from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution(object):
    def addMinimum(self, word):
        """
        :type word: str
        :rtype: int
        """
        ds="abc"
        for i in range(1,len(word)+1):
            s1 = ds*i
            cnt = 0
            for a in s1:
                if cnt < len(word) and word[cnt] == a:
                    cnt +=1
            if cnt == len(word):
                return len(s1) - len(word)
        





re =Solution()
print(re)