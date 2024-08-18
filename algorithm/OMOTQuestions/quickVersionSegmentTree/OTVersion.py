# https://leetcode.cn/contest/weekly-contest-411/problems/count-substrings-that-satisfy-k-constraint-ii/submissions/556409702/
from typing import List, Tuple, Optional
from collections import defaultdict,deque
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
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n = len(s)
        sg1= segment_tree([0]*n)
        sg2= segment_tree([0]*n)
        sg3= segment_tree([0]*n)
        m = len(queries)
        ret = [-1]*m
        dic2 = defaultdict(list)
        for i,(a,b) in enumerate(queries):
            dic2[b].append((i,a))
        
        dic = defaultdict(int)
        l = 0 
        for i,a in enumerate(s):
            dic[a] +=1
            while dic["0"] > k and dic["1"]>k:
                sg1.update(l,i-1)
                sg2.update(l,1)
                sg3.update(l,l)
                dic[s[l]] -=1
                l +=1
            for (idx,f) in dic2[i]:
                acc = (i-f+1)*(i-f+2)//2
                #print(acc,idx,f,i,sg2.query(f,i),sg1.query(f,i))
                acc -= sg2.query(f,i) * i - sg1.query(f,i)
                ret[idx] = acc
        return ret