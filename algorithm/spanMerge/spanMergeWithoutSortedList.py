#https://leetcode.cn/problems/count-integers-in-intervals/solution/chun-er-fen-by-migeater-t5kh/
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
        
        for i in range(lidx,ridx):
            left = min(left,span[i][0])
            right = max(right, span[i][1])
        span[lidx:ridx] = [(left,right)]

spn = Span()
print(spn.span)
spn.add(2,3)
print(spn.span)
spn.add(7,10)
spn.add(5,8)
print(spn.span)

