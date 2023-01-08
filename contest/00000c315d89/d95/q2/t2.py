from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
class DataStream(object):

    def __init__(self, value, k):
        """
        :type value: int
        :type k: int
        """
        self.value = value
        self.k = k 
        self.cnt =0


    def consec(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num ==self.value:
            self.cnt +=1
            if self.cnt >= self.k:
                return True
        else:
            self.cnt = 0 
        return False
        






re =Solution()
print(re)