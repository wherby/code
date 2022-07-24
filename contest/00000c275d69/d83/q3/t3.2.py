from sortedcontainers import SortedList
from collections import defaultdict

class NumberContainers(object):

    def __init__(self):
        self.vals =defaultdict(SortedList)
        self.dic={}


    def change(self, index, number):
        """
        :type index: int
        :type number: int
        :rtype: None
        """
        oldV = self.dic.get(index,-1)
        self.dic[index] = number
        if oldV != -1:
            self.vals[oldV].discard(index)
        self.vals[number].add(index)



    def find(self, number):
        """
        :type number: int
        :rtype: int
        """
        if len(self.vals[number]) !=0:
            return self.vals[number][0]
        return -1






re =Solution()
print(re)