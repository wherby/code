from typing import List, Tuple, Optional
import math

from math import ceil, log2

class segment_tree:
    # merge(left, right): function used to merge the two halves
    # basef(value): function applied on individual values
    # basev: identity for merge function, merger(value, basev) = value 
    # update(node_value, old, new): function to update the nodes
    def __init__(self, array, merge=lambda x,y:math.gcd(x,y), basev = 0, basef=lambda x:x):
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
    def minStable(self, nums: List[int], maxC: int) -> int:
        n = len(nums)
        dic ={}
        st = segment_tree(nums)
        for i in range(n):
            l,r = 0,i 
            while l<r:
                md = (l+r)>>1
                if st.query(md,i) ==1:
                    l= md+1 
                else:
                    r = md
            dic[i] = l
        #print(dic)
        def verify(md,c):
            lst = 0 
            cnt =0
            for i,a in enumerate(nums):
                lst = math.gcd(lst,a)
                #print(lst,"b",a,i)
                if lst >=2:
                    cnt +=1
                if cnt>md:
                    if c:
                        c -=1
                        cnt =0 
                        lst = 0 
                    else:
                        return False
                if lst ==1:
                    cnt = i-dic[i]+1
                    lst = st.query(dic[i],i)
                    #print(i,dic[i],cnt,"a",lst,a)
                #print(a,cnt,c,md)
            return True
        l ,r  = 0, n+1
        while l < r:
            md = (l+r)>>1
            #print(md,verify(md,maxC))
            if verify(md,maxC):
                r = md 
            else:
                l = md +1
        return l

from v1input import nums,maxC
re = Solution().minStable(nums,maxC)
print(re)