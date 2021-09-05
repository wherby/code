#https://leetcode.com/contest/weekly-contest-59/problems/my-calendar-i/
class MyCalendarTwo(object):

    def __init__(self):
    	self.lst=[]
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for item in self.lst:
        	start1,end1 =item
        	if start <= start1 and end >start1:
        		return False
        	if start <end1 and end>= end1:
        		return False
        	if start <= start1 and end >= end1:
        		return False
        	if start>= start1 and end <= end1:
        		return False
        self.lst.append([start,end])
        return True


MyCalendar= MyCalendarTwo();
ar=[[23,32],[42,50],[6,14],[0,7],[21,30],[26,31],[46,50],[28,36]]
for item in ar:
	print item
	start,end = item
	print MyCalendar.book(start,end),start,end