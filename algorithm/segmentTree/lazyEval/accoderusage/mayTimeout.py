# https://leetcode.cn/problems/longest-balanced-subarray-ii/submissions/672509816/
# timeout
from typing import List, Tuple, Optional
from collections import defaultdict,deque
# 手写 min max 更快
min = lambda a, b: b if b < a else a
max = lambda a, b: b if b > a else a


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

def createMaxMinSegTree(arr)->LazySegmentTree:
    def max_min_op(x,y):
        max_x,min_x= x 
        max_y,min_y =y 
        return (max(max_x,max_y),min(min_x,min_y))
    MAX_INF = float('inf')
    MIN_INF = float('-inf')
    E = ( MIN_INF,MAX_INF)
    # 3. mapping: 如何将懒标记 f (delta) 应用到数据 x (max, min)
    def max_min_mapping(f, x) :
        if f == ID:  # 优化：如果懒标记是单位元，直接返回
            return x
        
        max_val, min_val = x
        # 区间加 f，所以 max 和 min 都加 f
        return (max_val + f, min_val + f)

    # 4. composition: 如何合并新的懒标记 f 和旧的懒标记 g
    def max_min_composition(f, g) :
        # 懒标记是可累加的 (new_delta + old_delta)
        return f + g
    ID=0
    max_min_tree = LazySegmentTree(
    n=len(arr),
    op=max_min_op,
    e=E,
    mapping=max_min_mapping,
    composition=max_min_composition,
    id=ID)
    arr = [(a,a) for a in arr]
    max_min_tree.build(arr)
    return max_min_tree




import time


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0 
        name = func.__name__
        arg_str = ", ".join(repr(arg) for arg in args)
        print('[{0}] {1}' .format( elapsed, name))
        return result
    return clocked

@clock
def fx(a,b):
    acc = 0
    mod = 10**9+7
    for i in range(a*100):
        acc += a*b 
    return acc%mod 


class Solution:
    @clock
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        ls=[0]*(n+1)
        mmst = createMaxMinSegTree(ls)
        #print(mmst.get(2))
        dic= defaultdict(int)
        ret= acc = 0
        #print(n)
        for i,a in enumerate(nums,1):
            v = 1 if a %2  else -1 
            j = dic[a]
            if j ==0:
                acc += v 
                mmst.apply(i,n+1,v)
            else:
                mmst.apply(j,i, -v)
            dic[a] = i
            k = mmst.max_right(0,lambda x: not(x[0]>= acc>=x[1]))
            #print(k,acc,mmst.get(0),mmst.get(1),mmst.get(2),mmst.get(3),i,i-k)
            ret = max(ret,i-k)
        return ret

from input import nums

re =Solution().longestBalanced(nums)
print(re)