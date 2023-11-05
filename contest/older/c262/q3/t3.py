import heapq
from collections import defaultdict
class StockPrice(object):

    def __init__(self):
        self.mn=[]
        self.mx=[]
        self.curr = 0
        self.dic =defaultdict(int)
        self.removeDic =defaultdict(list)


    def update(self, timestamp, price):
        """
        :type timestamp: int
        :type price: int
        :rtype: None
        """
        told = self.dic[timestamp]
        self.removeDic[timestamp].append((told,timestamp))
        self.removeDic[timestamp] = list(filter(lambda x : x != (price,timestamp),self.removeDic[timestamp]))
        self.dic[timestamp] =price  
        self.curr = max(timestamp,self.curr)
        heapq.heappush(self.mn,(price,timestamp))
        heapq.heappush(self.mx,(-price,timestamp))


    def current(self):
        """
        :rtype: int
        """
        return self.dic[self.curr]


    def maximum(self):
        """
        :rtype: int
        """
        t1,timestamp =self.mx[0]
        while (-t1,timestamp)  in self.removeDic[timestamp] :
            heapq.heappop(self.mx)
            t1,timestamp =self.mx[0]
        return -t1


    def minimum(self):
        """
        :rtype: int
        """
        t1,timestamp = self.mn[0]
        while (t1,timestamp)  in self.removeDic[timestamp] :
            heapq.heappop(self.mn)
            t1,timestamp = self.mn[0]
        return t1



# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()


#["StockPrice","update","maximum","current","minimum","maximum","maximum","maximum","minimum","minimum","maximum","update","maximum","minimum","update","maximum","minimum","current","maximum","update","minimum","maximum","update","maximum","maximum","current","update","current","minimum","update","update","minimum","minimum","update","current","update","maximum","update","minimum"]
#[[],[38,2308],[],[],[],[],[],[],[],[],[],[47,7876],[],[],[58,1866],[],[],[],[],[43,121],[],[],[40,5339],[],[],[],[32,5339],[],[],[43,6414],[49,9369],[],[],[36,3192],[],[48,1006],[],[53,8013],[]]

#["StockPrice","update","maximum","current","minimum","maximum","maximum","maximum","minimum","minimum","maximum","update","maximum","minimum","update","maximum","minimum","current","maximum","update","minimum","maximum","update","maximum","maximum","current","update","current","minimum","update","update","minimum","minimum","update","current","update","maximum","update","minimum"]
#[[],[38,2308],[],[],[],[],[],[],[],[],[],[47,7876],[],[],[58,1866],[],[],[],[],[43,121],[],[],[40,5339],[],[],[],[32,5339],[],[],[43,6414],[49,9369],[],[],[36,3192],[],[48,1006],[],[53,8013],[]]

#[null,null,2308,2308,2308,2308,2308,2308,2308,2308,2308,null,7876,2308,null,7876,1866,1866,7876,null,121,7876,null,7876,7876,1866,null,1866,121,null,null,1866,2308,null,1866,null,9369,null,1006]
#[null,null,2308,2308,2308,2308,2308,2308,2308,2308,2308,null,7876,2308,null,7876,1866,1866,7876,null,121,7876,null,7876,7876,1866,null,1866,121,null,null,1866,1866,null,1866,null,9369,null,1006]