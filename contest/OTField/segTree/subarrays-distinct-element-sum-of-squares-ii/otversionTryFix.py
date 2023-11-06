from testInput import *

from typing import List, Tuple, Optional

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
        return ' '.join([str(x)  for x in self.tree])

    def _build_util(self, l, r, i, a):
        if(l==r):
            self.tree[i] = self.basef(a[l])
            return self.tree[i]
        mid = (l+r)//2
        self.tree[i] = self.merge(self._build_util(l,mid, 2*i+1, a), self._build_util(mid+1, r, 2*i+2, a))
        #print(i,self.tree[i])
        return self.tree[i]

    def build(self, a):
        self._build_util(0, len(a)-1, 0, a)

    def _query_util(self,  L, R, l, r,i):
        
        if L <=l <=r<=R:
            return self.tree[i]
        if L>r or R<l:
            return self.basev
        self.__pushDown(i,l,r) ## this code need to be fix for wrong
        mid = (l+r)>>1
        return self.merge(self._query_util(L,R,l, mid ,2*i+1),
                          self._query_util( L,R,mid+1, r,2*i+2))
     
                
    def __pushDown(self,i,l,r):
        if self.lazy[i]:
            #if l != r:
            self.lazy[2*i+1]= self.lazy[2*i+2] =True
            self.tracted[2*i+1] += self.tracted[i]
            self.tracted[2*i+2] += self.tracted[i]
        ## need to be changed
            mid = (l+r)>>1
            self.tree[i*2+1] += self.tracted[i]*(mid-l+1)
            self.tree[i*2+2] += self.tracted[i]*(r-mid)
            self.lazy[i] = False
            #self.tree[i] +=self.tracted[i]*(r-l+1)
            self.tracted[i]  =0
            
            
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
        
        if r < L or R <l:
            return
        if L <=l <=r<=R:
            self.lazy[root] = True
            self.tracted[root] += delta
            ## need to change
            self.tree[root] +=(r-l +1)*delta
            #self.__pushDown(root,l,r)
            return 
        self.__pushDown(root,l,r)
        mid = (l+r) >>1
        if L <= mid:
            self.__update(L,R,l,mid,2*root+1,delta)
        if R >= mid +1:
            self.__update(L,R,mid+1,r,2*root+2,delta)
        self.__pushUp(root)

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        mod = 10**9+7
        dic ={}# defaultdict(lambda:-1)
        n = len(nums)
        sm =0
        sg = segment_tree([0]*n)
        acc = 0
        for i,a in enumerate(nums):
            k= dic.get(a,-1)
            c = sg.query(k+1,i)
            sg.updateRange(k+1,i,1)
            #b = sg.query(k+1,i)
            acc +=c+c + i-k
            acc %=mod
            sm +=acc
            
            sm%=mod
            dic[a] =i
            #print(dic[a],b,c,sm,dic,a,k+1,i,"AA",sg)
            
        
        return (sm+mod)%mod
    
import time

start = time.time()
re =Solution().sumCounts(nums)
print(re)
end = time.time()
print(end - start)