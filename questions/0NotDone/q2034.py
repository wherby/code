# https://leetcode.com/contest/weekly-contest-262/problems/stock-price-fluctuation/
from sortedcontainers import SortedList

class StockPrice:

    def __init__(self):
        self.sl = SortedList()
        self.psl = SortedList()
        self.dic ={}

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.dic:
            val = self.dic[timestamp]
            self.sl.remove((timestamp,val))
            self.psl.remove((val,timestamp))
        self.sl.add((timestamp,price))
        self.psl.add((price,timestamp))
        self.dic[timestamp] =price

    def current(self) -> int:
        return self.sl[-1][1]

    def maximum(self) -> int:
        return self.psl[-1][0]
        

    def minimum(self) -> int:
        return self.psl[0][0]