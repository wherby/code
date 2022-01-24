from collections import defaultdict
import heapq

class StockPrice(object):

    def __init__(self):
        self.date=[]
        self.mn=[]
        self.mx =[]
        self.record =defaultdict(int)

    def update(self, timestamp, price):
        """
        :type timestamp: int
        :type price: int
        :rtype: None
        """
        self.record[timestamp] +=1
        heapq.heappush(self.date, (-timestamp,price,self.record[timestamp]))
        heapq.heappush(self.mn, (price,self.record[timestamp],timestamp))
        heapq.heappush(self.mx,(-price,self.record[timestamp],timestamp))



    def current(self):
        """
        :rtype: int
        """
        ts,price,record =self.date[0]
        while record != self.record[-ts]:
            heapq.heappop(self.date)
            ts,price,record =self.date[0]
        return price


    def maximum(self):
        """
        :rtype: int
        """
        price,record,ts=self.mx[0]
        while record != self.record[ts]:
            heapq.heappop(self.mx)
            price,record,ts =self.mx[0]
        return -price


    def minimum(self):
        """
        :rtype: int
        """
        price,record,ts=self.mn[0]
        while record != self.record[ts]:
            heapq.heappop(self.mn)
            price,record,ts =self.mn[0]
        return price
