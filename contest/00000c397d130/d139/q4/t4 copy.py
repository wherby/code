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


class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
        lls1,lls2 = [(0,0)],[(0,0)]
        a,b = tuple(coordinates[k])

        for x,y in coordinates:
            if x<a and y <b:
                lls1.append((a-x,b-y))
            if x > a and y > b:
                lls2.append((x-a,y-b))

        #print(lls1,lls2)
        def getNum(lls):
            dic2 = {}
            s1 =set()
            for x,y in lls:
                s1.add(y)
            for i,k in enumerate(sorted(s1)):
                dic2[k] =i

            dic = defaultdict(list)
            for x,y in lls:
                dic[x].append(y)
            arr =[0]*(len(dic)+10)
            seg = segment_tree(arr, merge=max)
            ret = 0
            key =sorted(dic.keys())
            for k in key:
                ls = dic[k]
                ls= list(set(ls))
                ls.sort(reverse=True)
                for b in ls:
                    b = dic2[b]
                    c = seg.query(0,b-1)
                    d = seg.query(0,b)
                    if c==d:
                        seg.update(b,c+1)
                    ret =max(ret,c+1)
            return ret
        return getNum(lls1) + getNum(lls2)-1







re =Solution().maxPathLength(coordinates = [[3,1],[2,2],[4,1],[0,0],[5,3]], k = 1)
print(re)