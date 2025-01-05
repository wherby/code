# https://leetcode.cn/problems/my-calendar-ii/description/?envType=daily-question&envId=2025-01-03

from collections import defaultdict,deque
class MyCalendarTwo:

    def __init__(self):
        self.dic = defaultdict(int)
        

    def book(self, startTime: int, endTime: int) -> bool:
        self.dic[startTime] +=1
        self.dic[endTime] -=1
        ks = list(self.dic.keys())
        acc =0 
        ks.sort()
        for k in ks:
            acc += self.dic[k]
            if acc >2:
                self.dic[startTime] -=1
                self.dic[endTime] +=1
                return False 
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)