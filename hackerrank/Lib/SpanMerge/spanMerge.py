def insert(intervals, newInterval):
    s, e = newInterval[0], newInterval[1]
    parts = merge, left, right = [], [], []
    for i in intervals:
        parts[(i[1] < s) - (i[0] > e)].append(i)
    if merge:
        s = min(s, merge[0][0])
        e = max(e, merge[-1][1])
    return left + [[s, e]] + right


intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,9]
print insert(intervals,newInterval)