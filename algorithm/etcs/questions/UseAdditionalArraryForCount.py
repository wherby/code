# https://leetcode.cn/problems/my-calendar-iii/submissions/
# Use cnt array for overlap range counting
import bisect

class MyCalendarThree:

    def __init__(self):
        self.points = []
        self.cnt = []
        self.k = 0


    def book(self, start: int, end: int) -> int:
        left = bisect.bisect_left(self.points,(start,1))
        self.points.insert(left,(start,1))
        self.cnt.insert(left,0)

        right = bisect.bisect_left(self.points,(end,-1))
        self.points.insert(right,(end,-1))
        self.cnt.insert(right,0)
        print(self.points,self.cnt)

        k = 0 if left == 0 else self.cnt[left-1]

        for i in range(left,right+1):
            k += self.points[i][1]
            self.cnt[i] = k 
            self.k = max(self.k, k)
        return self.k