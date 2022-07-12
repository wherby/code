import heapq
class SmallestInfiniteSet(object):

    def __init__(self):
        self.st =[]
        self.dic ={}
        for i in range(1,2000):
            heapq.heappush(self.st,i)
            self.dic[i] =1

    def popSmallest(self):
        """
        :rtype: int
        """
        a = heapq.heappop(self.st)
        self.dic[a] =0
        return a


    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.dic[num] ==0:
            heapq.heappush(self.st,num)
            self.dic[num]=1




re =Solution()
print(re)