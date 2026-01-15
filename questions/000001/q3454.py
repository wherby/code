#https://leetcode.cn/problems/separate-squares-ii/submissions/691256169/?envType=daily-question&envId=2026-01-14

from typing import List, Tuple, Optional
from collections import defaultdict,deque


class LazySegmentTree:
    """
    Reference
    https://github.com/atcoder/ac-library/blob/master/atcoder/lazysegtree.hpp
    https://github.com/atcoder/ac-library/blob/master/document_en/lazysegtree.md
    https://github.com/atcoder/ac-library/blob/master/document_ja/lazysegtree.md
    """
    def __init__(self, n, op, e, mapping, composition, id):
        self.n = n
        self.op = op
        self.e = e
        self.mapping = mapping
        self.composition = composition
        self.id = id
        self.log = (n - 1).bit_length()
        self.size = 1 << self.log
        self.d = [e] * (2 * self.size)
        self.lz = [id] * (self.size)

    def update(self, k):
        self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])

    def all_apply(self, k, f):
        self.d[k] = self.mapping(f, self.d[k])
        if k < self.size:
            self.lz[k] = self.composition(f, self.lz[k])

    def push(self, k):
        if self.lz[k] != self.id:
            self.all_apply(2 * k, self.lz[k])
            self.all_apply(2 * k + 1, self.lz[k])
            self.lz[k] = self.id

    def build(self, v):
        assert len(v) <= self.n
        for i in range(len(v)):
            self.d[self.size + i] = v[i]
        for i in range(self.size - 1, 0 ,-1):
            self.update(i)

    def set(self, p, x):
        assert 0 <= p < self.n
        p += self.size
        for i in range(self.log, 0, -1):
            self.push(p >> i)
        self.d[p] = x
        for i in range(1, self.log + 1):
            self.update(p >> i)

    def get(self, p):
        assert 0 <= p < self.n
        p += self.size
        for i in range(self.log, 0, -1):
            self.push(p >> i)
        return self.d[p]

    def prod(self, l, r):
        assert 0 <= l <= r <= self.n
        if l == r:
            return self.e
        l += self.size
        r += self.size
        for i in range(self.log, 0, -1):
            if (l >> i) << i != l:
                self.push(l >> i)
            if (r >> i) << i != r:
                self.push((r-1) >> i)
        sml = smr = self.e
        while l < r:
            if l & 1:
                sml = self.op(sml, self.d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op(self.d[r], smr)
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def all_prod(self):
        return self.d[1]

    # def apply(self, p, f):
    #     assert 0 <= p < self.n
    #     p += self.size
    #     for i in range(self.log, 0, -1):
    #         self.push(p >> i)
    #     self.d[p] = self.mapping(f, self.d[p])
    #     for i in range(1, self.log + 1):
    #         self.update(p >> i)
    
    # (2) It applies a[i] = f(a[i]) for all i = l..r-1.
    # 跟新的是前闭后开区间 [l,r)
    def apply(self, l, r, f):
        assert 0 <= l <= r <= self.n
        if l == r:
            return
        l += self.size
        r += self.size
        for i in range(self.log, 0, -1):
            if (l >> i) << i != l:
                self.push(l >> i)
            if (r >> i) << i != r:
                self.push((r - 1) >> i)
        l2 = l
        r2 = r
        while l < r:
            if l & 1:
                self.all_apply(l, f)
                l += 1
            if r & 1:
                r -= 1
                self.all_apply(r, f)
            l >>= 1
            r >>= 1
        l = l2
        r = r2
        for i in range(1, self.log + 1):
            if (l >> i) << i != l:
                self.update(l >> i)
            if (r >> i) << i != r:
                self.update((r - 1) >> i)

    # maxright: 从l 开始向右查询，找到第一个不符合g的
    def max_right(self, l, g):
        assert 0 <= l <= self.n
        assert g(self.e)
        #print(g,self.e)
        if l == self.n:
            return self.n
        l += self.size
        for i in range(self.log, 0, -1):
            self.push(l >> i)
        sm = self.e
        while True:
            while l % 2 == 0:
                l >>= 1
            #print(l,self.d[l],self.op(sm, self.d[l]))
            if not g(self.op(sm, self.d[l])):
                while l < self.size:
                    self.push(l)
                    l = 2 * l
                    if g(self.op(sm, self.d[l])):
                        sm = self.op(sm, self.d[l])
                        l += 1
                #print(sm)
                return l - self.size
            sm = self.op(sm, self.d[l])
            l += 1
            if (l & -l) == l:
                return self.n

    # 从r开始往左查询。查找最小符合g的l
    def min_left(self, r, g):
        assert 0 <= r <= self.n
        assert g(self.e)
        if r == 0:
            return 0
        r += self.size
        for i in range(self.log, 0, -1):
            self.push((r - 1) >> i)
        sm = self.e
        while True:
            r -= 1
            while r > 1 and r % 2:
                r >>= 1
            if not g(self.op(self.d[r], sm)):
                while r < self.size:
                    self.push(r)
                    r = 2 * r + 1
                    if g(self.op(self.d[r], sm)):
                        sm = self.op(self.d[r], sm)
                        r -= 1
                return r + 1 - self.size
            sm = self.op(self.d[r], sm)
            #print(sm,"sm",self.d[r],r)
            if (r & -r) == r:
                return 0
from itertools import pairwise
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        dic = defaultdict(list)
        vs = set()
        for a,b,c in squares:
            dic[b].append((1,a,a+c))
            dic[b+c].append((-1,a,a+c))
            vs.add(a)
            vs.add(a+c)
        keys = list(dic.keys())
        keys.sort()
        vs = list(vs)
        vs.sort()
        vd ={}
        for i,a in enumerate(vs):
            vd[a] = i 
        m = len(vd)
        def getLeastCover(vd):
               # (left,right,lowestCover,lowerstCoverLength)
            E = (10**20,0,10**10,0)
            def op(x,y):
                x1,x2,x3,x4 = x 
                y1,y2,y3,y4 = y 
                mc = min(x3,y3)
                mcl = (x4 if x3 ==mc else 0) + (y4 if y3 == mc else 0)
                return   (min(x1,y1),max(x2,y2),mc,mcl)
            def mapping(v,x):
                x1,x2,x3,x4 = x 
                return (x1,x2,x3+v,x4)
            def composition(x,y):
                return x+y
            segTree = LazySegmentTree(m,op,E,mapping,composition,0)
            v = []
            for a,b in pairwise(vd):
                v.append((a,b,0,b-a))
            #print(v)
            segTree.build(v)
            return segTree
        seg = getLeastCover(vd)
        records = []

        for a,b in pairwise(keys):
            for v,f,t in dic[a]:
                seg.apply(vd[f],vd[t], v)
            s,e,mc,mcl = seg.all_prod()
            unCovered = mcl if mc ==0 else 0
            #print(s,e,mc,mcl,a,b)
            records.append((e-s - unCovered,b,a))
        #print(records,vd)
        sm = 0 
        for w,t,f in records:
            sm += w*(t-f)
        acc = 0 
        for w,t,f in records:
            toAcc = acc +w*(t-f)
            if toAcc*2 >=sm:
                return f + (sm/2 - acc)/w
            acc =toAcc
            #print(acc,w,f,t)
            

re = Solution().separateSquares([[15,21,2],[19,21,3]])
print(re)