

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '[' + str(self.start) +"  , " + str(self.end ) + "]"


def insert(intervals, newInterval):
    s, e = newInterval.start, newInterval.end
    left = [i for i in intervals if i.end < s]
    right = [i for i in intervals if i.start > e]
    if left + right != intervals:
        s = min(s, intervals[len(left)].start)
        e = max(e, intervals[~len(right)].end)
    return left + [Interval(s, e)] + right


intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
intervals = map(lambda x: Interval(x[0],x[1]),intervals)
re=  insert(intervals,Interval(4,13))
print map(lambda x: str(x), re)