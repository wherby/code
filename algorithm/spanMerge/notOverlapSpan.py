# https://leetcode.cn/problems/my-calendar-i/
from bisect import bisect_right,bisect_left

class MyCalendar:
    def __init__(self):
        self.ls =[]



    def book(self, start: int, end: int) -> bool:
        l1 = bisect_right(self.ls,start)
        l2 = bisect_left(self.ls,end)
        if l1 ==l2 and l1 %2 ==0:
            self.ls = self.ls[:l1] +[start,end] +self.ls[l1:]
            return True
        else:
            return  False