# use node in segment_tree 
# Python will timeout https://leetcode-cn.com/problems/QO5KpG/submissions/
# https://leetcode-cn.com/submissions/detail/301027130/
from bisect import bisect_left, bisect_right
from math import ceil, log2



class segment_tree:
    # merge(left, right): function used to merge the two halves
    # basef(value): function applied on individual values
    # basev: identity for merge function, merger(value, basev) = value
    # update(node_value, old, new): function to update the nodes
    def __init__(self, array, merge=lambda x,y:x+y, basef=lambda x:x, basev = 0):
        self.merge = merge
        self.basef = basef
        self.basev = basev
        self.n = len(array)
        self.array = array
        m = ( 2**ceil(log2(len(array))+1) - 1 )
        self.tree = [0] * ( 2**ceil(log2(len(array))+1) - 1 )
        self.ass = [-1]*(m*2)
        self.sumadd = [0]*(m*2)
        #self.build(array)
    
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
#https://leetcode-cn.com/contest/season/2022-spring/ranking/solo/ OTTFF question 3
    def update(self, x, v):
        self._update_util( 0, 0, self.n-1, x, v )   
        self.array[x] =v 
    
    def apply_ass(self,o,v,l,r):
        self.ass[o] = v
        self.sumadd[o] = v*(r-l+1)
    
    def push(self,o,l,m,r):
        #print(o,self.ass)
        if self.ass[o] != -1:
            self.apply_ass(o*2 +1,self.ass[o],l,m)
            self.apply_ass(o*2 +2 ,self.ass[o],m+1,r)
            self.ass[o] =-1
    
    def pullup(self,o):
        self.sumadd[o] = self.sumadd[o*2+1] + self.sumadd[o*2+2]
        
    def update(self,o,l,r,fr,to,val):
        if fr <=l and r <= to:
            self.apply_ass(o,val,l,r)
            return
        m = (l+r)>>1
        self.push(o,l,m,r)
        if fr <=m:
            self.update(o*2+1,l,m,fr,to,val)
        if m <to:
            self.update(o*2 +2,m+1,r,fr,to,val)
        self.pullup(o)
        

class Solution(object):
    def getNumber(self, root, ops):
        """
        :type root: Optional[TreeNode]
        :type ops: List[List[int]]
        :rtype: int
        """
        ls = []
        def dfs(node):
            if node ==None:return
            dfs(node.left)
            ls.append(node.val)
            dfs(node.right)
        dfs(root)
        #print(ls)
        seg = segment_tree(ls)
        m =len(ls)
        #print(seg.sumadd[0])
        for op in ops:
            v,fr1,to1 = tuple(op)
            fr = bisect_left(ls,fr1)
            to = bisect_right(ls,to1)-1
            seg.update(0,0,m-1,fr,to,v)
            # print(seg.sumadd,fr,to)
            # print(seg.array)
            # print(seg.sumadd[0])
        return seg.sumadd[0]