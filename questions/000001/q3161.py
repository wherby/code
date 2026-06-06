from typing import List, Tuple, Optional
from sortedcontainers import SortedDict,SortedList
from bisect import bisect_right,insort_left,bisect_left


class SegTree:
    def __init__(self, size: int):
        self.n = 1
        while self.n < size:
            self.n <<= 1
        self.tree = [0] * (2 * self.n)

    def update(self, idx: int, val: int):
        idx += self.n
        self.tree[idx] = val
        idx >>= 1
        while idx:
            new_val = max(self.tree[2 * idx], self.tree[2 * idx + 1])
            if self.tree[idx] == new_val:
                break
            self.tree[idx] = new_val
            idx >>= 1

    def query(self, l: int, r: int) -> int:
        if l > r:
            return 0
        l += self.n
        r += self.n
        res = 0
        while l <= r:
            if l & 1:
                res = max(res, self.tree[l])
                l += 1
            if not (r & 1):
                res = max(res, self.tree[r])
                r -= 1
            l >>= 1
            r >>= 1
        return res

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        xs = list(set([q[1] for q in queries]))
        xs.sort()
        m = len(xs)
        sg = SegTree(m+2)
        dic = {}
        for i,a in enumerate(xs):
            dic[a] = i 
        #print(xs)
        sl = SortedList([0])
        ret = []
        for q  in queries:
            t = dic[q[1]]
            x = q[1]
            if q[0] ==1:
                k = sl.bisect_left(x)
                sg.update(t,x-sl[k-1])
                if k< len(sl):
                    t1= dic[sl[k]]
                    sg.update(t1,sl[k]-x)
                sl.add(x)
            else:
                sz = q[2]
                k = dic[x]
                t1 = sg.query(0,k)
                k1 = sl.bisect_left(x)
                t2 = x - sl[k1-1]
                #print(t1,t2,k1,sl,sg.tree)
                if max(t1,t2)>=sz:
                    ret.append(True)
                else:
                    ret.append(False)
        return ret

re = Solution().getResults([[1,1],[1,11],[1,4],[1,8],[2,13,7]])
print(re)