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
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        intervals2 = [(a,b,c,i) for i,(a,b,c) in enumerate(intervals)]
        intervals2.sort(key= lambda x:(x[1],x[3]))
        ls =set()
        for a,b,c in intervals:
            ls.add(a)
            ls.add(b)
            ls.add(a-1)
        ls = list(ls)
        ls.sort()
        od ={}
        for i,a in enumerate(ls):
            od[a] = i 
        n = len(ls)
        arr =[0]*n
        sg = segment_tree(arr, merge=max)
        sg2 = segment_tree(list(arr), merge=max)
        sg3 = segment_tree(list(arr), merge=max)
        dic = defaultdict(list)
        dic2 = defaultdict(list)
        dic3 = defaultdict(list)
        mx = 0
        ret =[]
        print(intervals2)
        for a,b, c,i in intervals2:
            bi =od[b]
            ai =od[a-1]
            if c + sg3.query(0,ai)==mx:
                r= [dic3[sg3.query(0,ai)] + [i]]
                if sorted(dic3[mx]) > sorted(r):
                    ret = r
            if c + sg3.query(0,ai)> mx:
                mx = c + sg3.query(0,ai)
                ret = [dic3[sg3.query(0,ai)] + [i]]
            if c + sg2.query(0,ai)==mx:
                r= [dic2[sg3.query(0,ai)] + [i]]
                if sorted(dic3[mx]) > sorted(r):
                    ret = r
            if c + sg2.query(0,ai) > sg3.query(0,bi):
                dic3[c+sg2.query(0,ai)] = dic2[sg2.query(0,ai)] +[i]
                sg3.update(bi,  c + sg2.query(0,ai) )
                if c + sg2.query(0,ai) > mx:
                    ret = [dic3[c+sg.query(0,ai)]]
                    mx =c + sg2.query(0,ai)
            if c + sg.query(0,ai)==mx:
                ret.append(dic[sg.query(0,ai)] + [i])
            if c + sg.query(0,ai) > sg2.query(0,bi):
                dic2[c+sg.query(0,ai)] = dic[sg.query(0,ai)] +[i]
                sg2.update(bi, c + sg.query(0,ai) )
                if c + sg.query(0,ai) > mx:
                    ret = [dic2[c+sg.query(0,ai)]]
                    mx =c+sg.query(0,ai)

            if c > sg.query(0,bi):
                dic[c] = [i]
                sg.update(bi,c)
                if c > mx:
                    ret = [[i]]
                    mx =c
        ret = [sorted(a) for a in ret]
        ret.sort()
        print(ret)
        return sorted(ret[0])





re =Solution().maximumWeight(intervals =[[8,15,32],[20,21,8],[8,16,29],[7,12,50],[16,25,27],[12,17,2],[8,12,45],[5,10,50]])
print(re)