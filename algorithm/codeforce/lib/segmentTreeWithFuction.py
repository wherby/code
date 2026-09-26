# # https://leetcode-cn.com/problems/range-sum-query-mutable/submissions/   verified time cost more than  setmentTreeImpl2.py
# reset basev when for merge =min
### alias
#    prod = query 这里特别注意，prod的区间应该是[l,r) 但是 query的区间是 [l,r],如果使用这里的 prod,则需要注意使用新定义的区间 [l,r]
from math import ceil, log2

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

    def set(self,x,y):
        self.update(x,y)

    def all_prod(self):
        return self.tree[0] 
    
    ## alias # 这里 prod的区间是[l,r]
    prod = query
    
    # def prod1(self,l,r):
    #     return self.query(l,r-1)

class SegTree:
    def __init__(self, merge, basev,array):
        if type(array) == list:
            self.seg = segment_tree(array,merge,basev)
        else:
            self.seg = segment_tree([basev]*array,merge,basev)
    
    def __getattr__(self, name):
        return getattr(self.seg,name)
    
    

if __name__ == '__main__':
    print("\nRange Sum with 8 node:")
    # Range Sum
    st = segment_tree([1,2,3,4,5,6,7,8])
    print(st)
    print(st.query(2,4))
    st.update(3,5)
    print(st.query(2,4))

    print("\nRange Sum with 9 node:")
    # Range Sum
    st = segment_tree([1,2,3,4,5,6,7,8,9])
    print(st)
    print(st.query(2,4))
    st.update(3,5)
    print(st.query(2,4))

    print("\nRange Max:")
    # Range Max
    st = segment_tree([1,2,3,4,5,6,7,8], max, basev=-float('inf'))
    print(st)
    print(st.query(2,4))
    st.update(3,6)
    print(st.query(2,4))

    print("\nRange Min:")
    # Range Max
    st = segment_tree([1,2,3,4,5,6,7,8], min,basev=float('inf'))
    print(st)
    print(st.query(2,4))
    st.update(3,1)
    print(st.query(2,4))