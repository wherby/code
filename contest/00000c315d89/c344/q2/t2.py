from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
class FrequencyTracker:

    def __init__(self):
        self.fdic = defaultdict(int)
        self.dic = defaultdict(int)


    def add(self, number: int) -> None:
        self.fdic[self.dic[number]] -=1
        self.fdic[self.dic[number] +1] +=1
        self.dic[number] +=1

    def deleteOne(self, number: int) -> None:
        if self.dic[number]>0:
            self.fdic[self.dic[number]] -=1
            self.dic[number]-=1
            self.fdic[self.dic[number]] +=1


    def hasFrequency(self, frequency: int) -> bool:
        return self.fdic[frequency] >0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)




re =Solution()
print(re)