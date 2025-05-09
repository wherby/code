# https://leetcode.cn/problems/minimum-cost-to-split-an-array/
# Range update min-max

from typing import List, Tuple, Optional


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
        if L<=l<=r<=R:
            return self.tree[i]
        if l>R or r<L:
            return self.basev
        self.__pushDown(i,L,R)
        return self.merge( self._query_util( 2*i+1, l, (l+r)//2, L, R ),
                          self._query_util( 2*i+2, (l+r)//2+1, r, L, R ) )
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
        if L <=l <=r<=R:
            self.lazy[root] = True
            self.tracted[root] += delta
            ## need to change
            self.tree[root] +=delta
            return 
        self.__pushDown(root,l,r)
        mid = (l+r) >>1
        if L <= mid:
            self.__updateRange(L,R,l,mid,2*root+1,delta)
        if R >= mid +1:
            self.__updateRange(L,R,mid+1,r,2*root+2,delta)
        self.__pushUp(root)
            

from collections import defaultdict,deque
class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        ans = 0 
        last = defaultdict(int)
        last2 = defaultdict(int)
        n = len(nums)
        st = SegmentTree([0]*n*2, merge=min)
        for i,x in enumerate(nums,1):
            st.updateRange(i,i,ans)
            st.updateRange(last[x]+1,i,-1)
            if last[x]:
                st.updateRange(last2[x]+1,last[x],1)
            ans = k + st.query(1,i)
            last2[x] = last[x]
            last[x] = i 
        #print(ans)
        return ans +len(nums)


re =Solution().minCost(nums = [1,2,1,2,1,3,3], k = 2)
#re =Solution().minCost(nums = [1,2,1,2,1], k = 5)
print(re)