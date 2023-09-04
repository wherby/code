# https://leetcode.cn/problems/insert-interval/description/
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        intervals.append([newInterval[0],newInterval[1]])
        intervals =  sorted(intervals,reverse =True)
        while intervals:
            left,right = intervals.pop()
            while intervals and right >= intervals[-1][0]:
                _,b = intervals.pop()
                right = max(right,b)
            ret.append([left,right])
        return ret