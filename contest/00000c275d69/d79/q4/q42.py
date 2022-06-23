# https://leetcode.cn/problems/booking-concert-tickets-in-groups/
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

class CombineSegTree():
    def __init__(self,arr):
        self.sumTree= segment_tree(arr)
        self.mxTree = segment_tree(arr,max, basev=-float('inf'))
    
    def update(self,idx,val):
        self.sumTree.update(idx,val)
        self.mxTree.update(idx,val)

class BookMyShow:

    def __init__(self, n: int, m: int):
        self.full =0
        self.m = m
        self.comb = CombineSegTree([m]*n)
        


    def gather(self, k: int, maxRow: int) :
        l = 0
        r = maxRow
        if self.comb.mxTree.query(l,r) <k:
            return []
        
        while l<r:
            mid =(l+r)>>1
            if self.comb.mxTree.query(l,mid)<k:
                l= mid+1
            else:
                r = mid 
        #print(l,self.comb.mxTree.array,self.comb.mxTree.query(l,r),k)
        if self.comb.mxTree.array[l] <k:
            return []
        ret = self.comb.mxTree.array[l]
        self.comb.update(l,ret-k)
        return [l,self.m-ret]


    def scatter(self, k: int, maxRow: int) -> bool:
        ret = self.comb.sumTree.query(0,maxRow)
        #print(ret,"xx")
        if ret <k:
            return False
        else:
            for i in range(self.full,maxRow+1):
                rmd = min(k,self.comb.mxTree.array[i])
                #print(rmd,self.mxTree.array[i],k)
                if rmd >0:
                    k -= rmd 
                    self.comb.update(i,self.comb.mxTree.array[i]-rmd )
                if self.comb.mxTree.array[i] ==0:
                    self.full +=1
            return True



# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)
re = BookMyShow(5,9)
print(re.scatter(3,3))
##print(re.mxTree.array,re.ftTree.bit)
#print(re.gather(7,2))
print(re.gather(9,1))
#print(re.mxTree.array,re.ftTree.bit)
print(re.scatter(5,1))
#print(re.mxTree.array,re.ftTree.bit)