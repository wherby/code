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


class SegmentTree:
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
        self.n4 = 4*self.n
        self.tree = [0] * self.n4
        self.lazy = [False] * self.n4
        self.tracted= [0] * self.n4
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

    def _query_util(self, i, l, r, L, R):
        self.__pushDown(i,l,r)
        if L<=l<=r<=R:
            return self.tree[i]
        if l>R or r<L:
            return self.basev
        
        return self.merge( self._query_util( 2*i+1, l, (l+r)//2, L, R ),
                          self._query_util( 2*i+2, (l+r)//2+1, r, L, R ) )
    
    def __pushDown(self,i,l,r):
        if self.lazy[i] :
            ## need to be changed
            self.tree[i] += self.tracted[i]
            if l !=r:
                self.lazy[2*i+1]= self.lazy[2*i+2] =True
                self.tracted[2*i+1] += self.tracted[i]
                self.tracted[2*i+2] += self.tracted[i]
  
            self.lazy[i] = False
            self.tracted[i]  =0
            
            
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

    def updateTo(self, x, v):
        self._update_util( 0, 0, self.n-1, x, v )   
        self.array[x] =v 
    
    def updateRange(self,left,right,delta):
        self.__updateRange(left,right,0,self.n-1,0,delta)
        
    def __pushUp(self,root):
        self.tree[root] = self.merge(self.tree[2*root+1],self.tree[2*root+2])        

    def __updateRange(self,L,R,l,r,root,delta):

        
        self.__pushDown(root,l,r)
        if L <=l <=r<=R:
            self.lazy[root] = True
            self.tracted[root] += delta
            ## need to change
            #self.tree[root] +=delta
            self.__pushDown(root,l,r)
            return 
        if l>R or r<L:
            return
        mid = (l+r) >>1
        self.__updateRange(L,R,l,mid,2*root+1,delta)
        self.__updateRange(L,R,mid+1,r,2*root+2,delta)
        self.__pushUp(root)


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        seg = SegmentTree(nums,merge=max)
        if max(nums) ==0:
            return 0
        for i,(a,b,c) in enumerate(queries):
            #@print(seg.query(0,n-1))
            seg.updateRange(a,b,-c)
           #print(a,b,c, seg.query(0,n-1))
            if seg.query(0,n-1) <=0:
                return i+1
            
        return -1




re =Solution().minZeroArray( nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]])
print(re)