# https://leetcode.cn/problems/count-substrings-that-satisfy-k-constraint-ii/
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq

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


    def __pushDown(self,i,l,r):
        if self.lazy[i]:
            if l != r:
                self.lazy[2*i+1]= self.lazy[2*i+2] =True
                self.tracted[2*i+1] += self.tracted[i]
                self.tracted[2*i+2] += self.tracted[i]
            ## need to be changed
            self.lazy[i] = False
            self.tree[i] +=self.tracted[i]*(r-l+1)
            self.tracted[i]  =0

    def _query_util(self,  L, R, l, r,i):
        self.__pushDown(i,l,r) ## this code fixed
        if L <=l <=r<=R:
            return self.tree[i]
        if L>r or R<l:
            return self.basev
        
        mid = (l+r)>>1
        return self.merge(self._query_util(L,R,l, mid ,2*i+1),
                          self._query_util( L,R,mid+1, r,2*i+2))

    def query(self, left, right):
        return self._query_util(left,right,0,self.n-1,0)

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
        self.__update(left,right,0,self.n-1,0,delta)
        
    def __pushUp(self,root):
        self.tree[root] = self.merge(self.tree[2*root+1],self.tree[2*root+2])        

    def __update(self,L,R,l,r,root,delta):
        self.__pushDown(root,l,r)
        if r < L or R <l:
            return
        if L <=l <=r<=R:
            self.lazy[root] = True
            self.tracted[root] += delta
            ## need to change
            self.__pushDown(root,l,r)
            return 
        mid = (l+r) >>1
        self.__update(L,R,l,mid,2*root+1,delta)
        self.__update(L,R,mid+1,r,2*root+2,delta)
        self.__pushUp(root)

  
    
    
    ## from https://leetcode.cn/contest/weekly-contest-336/ranking/  	5cm/s 
    def __pushDownSetValue(self,i,l,r):
        if self.lazy[i]:
            self.lazy[2*i+1] = self.lazy[2*i+2] = True
            self.tracted[2*i+1] = self.tracted[2*i+2] = self.tracted[i]
            self.lazy[i] = False
            mid = (l+r)>>1
            self.tree[2*i+1] =(mid-l+1) *self.tracted[i]
            self.tree[2*i+2] =(r- mid) *self.tracted[i]
            self.tracted[i]=0
            
    def updateRangeSetValue(self,left,right,value):
        self.__updateRangeSetValue(left,right,0,self.n-1,0,value)
    
    def __updateRangeSetValue(self,L,R,l,r,root,value):
        if L <=l<=r<=R:
            #print(R,L,value)
            self.tree[root] =(r-l+1)*value
            self.lazy[root] =True
            self.tracted[root] = value
            return 
        self.__pushDownSetValue(root,l,r)
        mid = (l+r)>>1
        if(mid>=L):
            self.__updateRangeSetValue(L,R,l,mid,2*root+1,value)
        if R>mid:
            self.__updateRangeSetValue(L,R,mid+1,r,2*root+2,value)
        self.__pushUp(root)


    def _query_utilSetValue(self, i, ln, rn, l, r):
        if l<=ln<=rn<=r:
            return self.tree[i]
        if ln>r or rn<l:
            return self.basev
        self.__pushDownSetValue(i,ln,rn)
        return self.merge( self._query_utilSetValue( 2*i+1, ln, (ln+rn)//2, l, r ),
                          self._query_utilSetValue( 2*i+2, (ln+rn)//2+1, rn, l, r ) )
                
    def querySetValue(self, l, r):
        return self._query_utilSetValue( 0, 0, self.n-1, l, r )  
    
    def bound(self,val,l,r):
        if l==r:
            return l
        mid = (l+r)>>1
        lc = self.__bound(mid+1,r)
        if lc >=val:
            return self.bound(val,mid+1,r)
        else:
            return self.bound(val-lc,l,mid)
    
    def __bound(self,l,r):
        return r-l +1 -self.querySetValue(l,r)
        

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        dic= defaultdict(list)
        for i,(a,b) in enumerate(queries):
            dic[b].append((i,a))
        ls =[0]*2
        l = 0
        s = [int(a) for a in s]
        m = len(queries)
        ret = [-1]*m
        n = len(s)
        seg = segment_tree([0]*n)
        #print(dic)
        for i,a in enumerate(s):
            ls[a] +=1
            while ls[0] > k and ls[1] > k:
                ls[s[l]] -=1
                l +=1
            #print(l,i,ls)
            seg.updateRange(l,i,1)
            for idx,b in dic[i]:

                ret[idx] = seg.query(b,i)
               
        return ret

re =Solution().countKConstraintSubstrings(s = "010101", k = 1, queries = [[0,5],[1,4],[2,3]])
print(re)