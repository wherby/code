from email.policy import default
from typing import DefaultDict


import heapq
class NumberContainers(object):

    def __init__(self):
        self.dic =DefaultDict(list)
        self.vals = {}


    def change(self, index, number):
        """
        :type index: int
        :type number: int
        :rtype: None
        """
        self.vals[index] = number
        heapq.heappush(self.dic[number],index)


    def find(self, number):
        """
        :type number: int
        :rtype: int
        """
        while len(self.dic[number])>0:
            a = heapq.heappop(self.dic[number])
            if self.vals[a] == number:
                heapq.heappush(self.dic[number],a)
                return a 
        return -1





re =Solution()
print(re)