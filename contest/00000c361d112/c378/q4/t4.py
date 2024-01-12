from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf
from collections import Counter


from math import ceil, log2

class segment_tree:
    # merge(left, right): function used to merge the two halves
    # basef(value): function applied on individual values
    # basev: identity for merge function, merger(value, basev) = value
    # update(node_value, old, new): function to update the nodes
    def __init__(self, array, merge=lambda x,y:x+y, basev = 0, basef=lambda x:x):
        self.merge = merge
        self.basef = basef
        self.basev = basev
        self.n = len(array)
        self.array = array
        self.tree = [0] * ( 2**ceil(log2(len(array))+1) - 1 )
        self.build(array)
    
    def __str__(self):
        return ' '.join([str(x) for x in self.tree])

    def _build_util(self, l, r, i, a):
        if(l==r):
            self.tree[i] = self.basef(a[l])
            return self.tree[i]
        mid = (l+r)//2
        self.tree[i] = self.merge(self._build_util(l,mid, 2*i+1, a), self._build_util(mid+1, r, 2*i+2, a))
        return self.tree[i]

    def build(self, a):
        self._build_util(0, len(a)-1, 0, a)

    def _query_util(self, i, ln, rn, l, r):
        if ln>=l and rn<=r:
            return self.tree[i]
        if ln>r or rn<l:
            return self.basev
        return self.merge( self._query_util( 2*i+1, ln, (ln+rn)//2, l, r ), self._query_util( 2*i+2, (ln+rn)//2+1, rn, l, r ) )

    def query(self, l, r):
        return self._query_util( 0, 0, self.n-1, l, r )

    def _update_util(self, i, ln, rn, x, v):
        if x>=ln and x<=rn:
            if ln != rn:
                self._update_util( 2*i+1, ln, (ln+rn)//2, x, v )
                self._update_util( 2*i+2, (ln+rn)//2 + 1, rn, x, v )
                self.tree[i] = self.merge(self.tree[2*i+1], self.tree[2*i+2])
            else:
                self.tree[i] = self.basef(v)

    def update(self, x, v):
        self._update_util( 0, 0, self.n-1, x, v )   
        self.array[x] =v         

from sortedcontainers import SortedList
from bisect import bisect_right,bisect_left
## Merge on continue [[1,1][2,2]] will  merge
class Span():
    def __init__(self):
        self.span =SortedList([(-2,-2),(10**10,10**10)])
    
    def add(self,left,right):
        leftIdx = bisect_left(self.span,(left,0))
        leftIdx -=1
        if self.span[leftIdx][1] <left-1:
            leftIdx +=1
        remove=[]
        endIdx = leftIdx
        while  endIdx < len(self.span) and self.span[endIdx][0] <=right +1:
            remove.append(self.span[endIdx])
            endIdx +=1
        newLeft,newRight = left,right
        for item in remove:
            newLeft = min(newLeft,item[0])
            newRight = max(newRight,item[1])
            self.span.remove(item)
        self.span.add((newLeft,newRight))

class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n2 = len(s)
        m = len(queries)
        c1,c2= Counter(s[:n2//2]),Counter(s[n2//2:])
        if c1 != c2 :
            return [False] *m
        diff= []
        arr=[0]*(n2//2)
        sg = segment_tree(arr)
        for i in range(n2//2):
            if s[i] != s[n2-1-i]:
                sg.update(i,1)
        sm = sg.query(0,n2//2 -1)
        sgs = [segment_tree([0]*n2) for _ in range(26)]
        def getO(a):
            return ord(a) - ord('a')
        for i in range(n2//2):
            if s[i] != s[n2-1-i]:
                sgs[getO(s[i])].update(i,1)
                sgs[getO(s[n2-1-i])].update(i,-1)
                sgs[getO(s[n2-1-i])].update(n2-1-i,1)
                sgs[getO(s[i])].update(n2-1-i,-1)
        ret = []
        #print(sm)
        for a,b,c,d in queries:
            c1,d1 = n2-1-c,n2-1-d
            sp = Span()
            sp.add(a,b)
            sp.add(d1,c1)
            m = len(sp.span)
            tp = 0
            for i in range(1,m-1):
                f,t = sp.span[i]
                tp += sg.query(f,t)
            #print(tp,sm,sp.span)
            if sg.query(a,b) ==sm:
                ret.append(True)
            elif sg.query(d1,c1) == sm:
                ret.append(True)
                
            elif tp == sm:
                isG = True
                for i in range(26):
                    tp = 0 
                    tp += sgs[i].query(a,b)
                    tp += sgs[i].query(c,d)
                    if tp !=0:
                        isG = False
                ret.append(isG)
            else:
                ret.append(False)
        return ret





re =Solution().canMakePalindromeQueries("odaxusaweuasuoeudxwa",[[0,5,10,14]])
print(re)