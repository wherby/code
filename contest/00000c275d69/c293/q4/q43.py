#https://leetcode.cn/problems/count-integers-in-intervals/
from bisect import bisect_right,bisect_left
class Span:
    def __init__(self):
        self.span = []
        
    def add(self,left,right):
        span = self.span
        # 找最左侧的与[left,right]相交的区间[l,r], r大到一定程度才会相交
        lidx = bisect_left(span,left,key=lambda itv:itv[1])
        # 找最右侧的与[left,right]相交的区间[l,r], l大到一定程度才不相交
        ridx = bisect_right(span,right,key=lambda itv:itv[0])
        
        acc=0
        for i in range(lidx,ridx):
            left = min(left,span[i][0])
            right = max(right, span[i][1])
            acc += span[i][1]-span[i][0]+1
        span[lidx:ridx] = [(left,right)]
        return right-left +1 -acc


class CountIntervals(object):

    def __init__(self):
        self.cnt = 0
        self.sp = Span()


    def add(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        ac= self.sp.add(left,right)
        self.cnt += ac

    def count(self):
        """
        :rtype: int
        """
        return self.cnt


# re = CountIntervals()
# re.add(39,44)
# re.add(13,49)
# print(re.count())
# re.add(47,50)
# print(re.count())
# print(re.sp.span)

# re = CountIntervals()
# re.add(2,3)
# re.add(7,10)
# print(re.count())
# re.add(5,8)
# print(re.count())
# print(re.sp.span)

re = CountIntervals()
re.add(5,10)
print(re.count())
print(re.sp.span)
re.add(5,10)
print(re.count())
print(re.sp.span)