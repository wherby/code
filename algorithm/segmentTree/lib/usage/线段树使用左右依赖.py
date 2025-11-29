from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf


mod = 10**9+7
class SegmentTree:
    def __init__(self, op=max, e=lambda: -float("inf"), a=[]):

        self.n = n = len(a)
        self.op, self.e = op, e
        self.leafN = 1
        while n > self.leafN:
            self.leafN <<= 1
        self.offset = self.leafN

        self.x = [e for _ in range(self.leafN << 1)]
        if a:
            self.x[self.offset : self.offset + n] = a[:]
            l = self.offset
            r = l + self.leafN
            while 1 < l:
                for i in range(l, r, 2):
                    self.x[i >> 1] = op(self.x[i], self.x[i + 1])
                l >>= 1
                r >>= 1

    def get_value(self, i):

        return self.x[self.offset + i]

    def tolist(self):
        res = []
        for i in range(self.n):
            res.append(self.get_value(i))
        return res

    def set_value(self, i, val):

        i += self.offset
        self.x[i] = val
        while 1 < i:
            i >>= 1
            j = i << 1
            self.x[i] = self.op(self.x[j], self.x[j + 1])

    def prod(self, l, r):

        l += self.offset
        r += self.offset
        val_l, val_r = self.e, self.e
        while l < r:
            if l & 1:
                val_l = self.op(val_l, self.x[l])
                l += 1
            if r & 1:
                r -= 1
                val_r = self.op(self.x[r], val_r)
            l >>= 1
            r >>= 1
        return self.op(val_l, val_r)


    def max_right(self, i, check_func):

        i += self.offset
        if not check_func(self.x[i]):
            return -1
        val_l = self.e
        while True:
            i //= i & -i
            temp = self.op(val_l, self.x[i])
            if not check_func(temp):
                while i < self.offset:
                    i <<= 1
                    temp = self.op(val_l, self.x[i])
                    if check_func(temp):
                        val_l = temp
                        i += 1
                return i - 1 - self.offset
            val_l = temp
            i += 1
            if i & -i == i:
                return self.n - 1
    
    def min_left(self, r, g):
        assert 0 <= r <= self.n
        assert g(self.e)
        if r == 0:
            return 0
        r += self.offset
        sm = self.e
        while True:
            r -= 1
            while r > 1 and r % 2:
                r >>= 1
            if not g(self.op(self.x[r], sm)):
                while r < self.offset:
                    r = 2 * r + 1
                    if g(self.op(self.x[r], sm)):
                        sm = self.op(self.x[r], sm)
                        r -= 1
                return r + 1 - self.offset
            sm = self.op(self.x[r], sm)
            #print(sm,"sm",self.d[r],r)
            if (r & -r) == r:
                return 0

    def min_right(self, i, check_func):

        ret = self.max_right(i, lambda x: not check_func(x))
        if ret == self.n - 1:
            return -1
        if ret < 0:
            return i
        return ret + 1

    def max_left(self, j, check_func):

        ret = self.min_left(j, lambda x: not check_func(x))
        if ret < 0:
            return j
        return ret - 1

    def __setitem__(self, k: int, key):
        self.set_value(k, key)

    def __getitem__(self, k: int):
        return self.get_value(k)

    def __len__(self):
        return self.n

    def __str__(self):
        return str(self.tolist())

    def __bool__(self):
        return self.n != 0

    def __repr__(self):
        return f"SegmentTree({self.tolist()})"

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        ls =[]
        for a in s :
            a = int(a)
            ls.append([a,a,int(a!=0)])
        def merge(A,B):
            pre1,sm1,cnt1 = A 
            pre2,sm2,cnt2 = B 
            pre3 = pre1 *pow(10,cnt2,mod) + pre2
            sm3 = sm1+sm2
            cnt3 = cnt1 +cnt2 
            return [pre3,sm3,cnt3]
        st = SegmentTree(op=merge,e=[0,0,0],a = ls)
        ret = []
        for f,t in queries:
            c= st.prod(f,t+1)
            ret.append(c[0]*c[1]%mod)
        return ret
        






s = "83653355979889175588"
queries =[[0,2],[0,8],[0,10],[0,11],[0,13],[0,14],[0,15],[0,19],[1,4],[1,5],[1,6],[1,12],[1,16],[1,17],[1,18],[2,4],[2,5],[2,7],[2,9],[2,10],[2,11],[2,14],[2,19],[3,5],[3,7],[3,9],[3,10],[3,14],[3,15],[3,16],[4,9],[4,10],[4,15],[4,16],[4,18],[4,19],[5,6],[5,12],[5,14],[6,7],[6,8],[6,9],[6,10],[6,14],[6,15],[6,19],[7,9],[7,11],[7,13],[7,15],[7,17],[7,18],[8,8],[8,10],[8,12],[8,13],[8,18],[9,9],[9,10],[9,11],[9,13],[9,14],[9,15],[9,16],[9,19],[10,10],[10,14],[10,15],[10,19],[11,12],[11,19],[12,13],[12,16],[13,16],[13,17],[13,19],[14,14],[15,16],[15,17],[18,18]]

re =Solution().sumAndMultiply(s , queries )
exc = [14212,317077000,161389787,882329907,274699767,300940897,785430555,513914994,62101,730660,9133375,827275582,751358554,229370145,746249343,9142,111061,17640585,809430657,974510677,13585136,660746179,40897448,5863,1120455,197417089,454375020,305251240,238173859,279317386,10739104,137595139,251006020,409388971,764290238,568372898,280,922291345,827127435,550,10621,145522,1959265,147732113,663243696,545670509,12537,2272324,328893895,673301512,319067560,101983139,81,24475,4017508,48994450,157682279,49,1264,19152,3275449,33553422,391456933,314015422,688127163,81,3461185,41534514,463935280,1408,461359328,1513,2675250,201850,2477385,394550284,1,900,12835,64]

print(re)
print(exc)
print(re==exc)