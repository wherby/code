# https://leetcode.cn/problems/count-substrings-that-satisfy-k-constraint-ii/
# Range update  sum question 
# will Time out using algorithm/segmentTree/segTreeWIthRange/q3261.py will pass
# https://leetcode.cn/problems/count-substrings-that-satisfy-k-constraint-ii/submissions/580201592/?envType=daily-question&envId=2024-11-13
from typing import List, Tuple, Optional
from collections import defaultdict,deque

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
            self.tree[i] += (r-l+1)*self.tracted[i]
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
        # if not(l >R or mid<l) :
        #     self.__updateRange(L,R,l,mid,2*root+1,delta)

        # if not(mid+1 >R or r <L):
        #     self.__updateRange(L,R,mid+1,r,2*root+2,delta)
        self.__updateRange(L,R,l,mid,2*root+1,delta)
        self.__updateRange(L,R,mid+1,r,2*root+2,delta)
        #self.tree[root] = self.merge(self.tree[2*root+1],self.tree[2*root+2])
        self.__pushUp(root)

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
        seg = SegmentTree([0]*n)
        #print(dic)
        for i,a in enumerate(s):
            ls[a] +=1
            while ls[0] > k and ls[1] > k:
                ls[s[l]] -=1
                l +=1
            #print(l,i,ls)
            seg.updateRange(l,i,1)
            # ss=[]
            # for j in range(5):
            #     ss.append(seg.query(j,j))
            # print(ss)
            for idx,b in dic[i]:

                ret[idx] = seg.query(b,i)
               
        return ret

re =Solution().countKConstraintSubstrings(s = "010101", k = 1, queries = [[0,5],[1,4],[2,3]])
print(re)