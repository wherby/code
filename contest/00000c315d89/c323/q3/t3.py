from typing import List, Tuple, Optional

from math import ceil, log2
from collections import defaultdict,deque

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

class Allocator:

    def __init__(self, n: int):
        self.ls = [0]*n
        self.st = segment_tree(self.ls)
        self.n = n
        self.start =0
        self.dic= defaultdict(list)

    def allocate(self, size: int, mID: int) -> int:
        start =self.start
        #print(size,mID,self.st.array)
        while  start + size<= self.n:
            if self.st.query(start,start+size-1)  ==0:
                for i in range(size):
                    self.dic[mID].append(start+i)
                    self.ls[start+i] = mID
                    if start+i == self.start:
                        self.start +=1
                self.st = segment_tree(self.ls)
                return start
            start +=1
        return -1
        


    def free(self, mID: int) -> int:
        cnt =0
        for i in self.dic[mID]:
            self.ls[i] = 0
            cnt +=1
            self.start = min(self.start,i)
        self.st = segment_tree(self.st.array)
        self.dic[mID] = []
        return cnt
        







re =Solution()
print(re)