# Verified
# https://leetcode.cn/contest/weekly-contest-336/problems/minimum-time-to-complete-all-tasks/

# code with Bug for https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/D/my-submissions?source=facebook
# contest\meta2023\r1\q4\qn copy.py

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
            self.lazy[2*i+1]= self.lazy[2*i+2] =True
            self.tracted[2*i+1] += self.tracted[i]
            self.tracted[2*i+2] += self.tracted[i]
            self.lazy[i] = False
            ## need to be changed
            self.tree[i*2+1] += self.tracted[i]
            self.tree[i*2+2] += self.tracted[i]
            self.tracted[i]  =0

    def _query_util(self,  L, R, l, r,i):
        if L <=l <=r<=R:
            return self.tree[i]
        if L>r or R<l:
            return self.basev
        self.__pushDown(i,l,r) ## this code need to be fix for wrong
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
        if L <=l <=r<=R:
            self.lazy[root] = True
            self.tracted[root] += delta
            ## need to change
            self.tree[root] +=delta
            return 
        self.__pushDown(root,l,r)
        mid = (l+r) >>1
        if L <= mid:
            self.__update(L,R,l,mid,2*root+1,delta)
        if R >= mid +1:
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
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        ls=[0]*2002
        sg =segment_tree(ls)
        tasks.sort(key=lambda x: x[1])
        for s,e,c in tasks:
            val = sg.querySetValue(s,e)
            #print(val,s,e)
            if val >=c:continue
            id = sg.bound(c-val,s,e)
            sg.updateRangeSetValue(id,e,1)
            #print(s,e,c,id,sg.querySetValue(0,2000),sg.querySetValue(9,15))
            #print(s,e,c,id)
            #print(sg.tree[0])
        return sg.query(0,2000)
        
        
        
            
        
        
        





#re =Solution().findMinimumTime(tasks = [[1,10,7],[4,11,1],[3,19,7],[10,15,2]])
re =Solution().findMinimumTime([[14,17,2],[2,15,11],[5,18,2]])
print(re)
