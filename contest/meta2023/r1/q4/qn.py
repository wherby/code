#https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c
# Not finished Bug 
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin

mod  =10**9+7
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
        self.toggledValue =[[0,0] for _ in range(self.n4)]
        self.build(array)
    
    def __str__(self):
        return ' '.join([str(x) for x in self.tree])

    def _build_util(self, l, r, i, a):
        if(l==r):
            self.tree[i] = self.basef(a[l])
            self.toggledValue[i] = [self.tree[i], mod - self.tree[i]]
            return self.tree[i]
        mid = (l+r)//2
        self.tree[i] = self.merge(self._build_util(l,mid, 2*i+1, a), self._build_util(mid+1, r, 2*i+2, a))
        self.toggledValue[i] = [self.tree[i], mod - self.tree[i]]
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
            self.lazy[2*i+1]= self.lazy[2*i+2] =True
            self.tracted[2*i+1] += self.tracted[i]
            self.tracted[2*i+2] += self.tracted[i]
            self.lazy[i] = False
            ## need to be changed
            self.tree[i*2+1] =self.toggledValue[i*2+1][self.tracted[i*2+1] %2]
            self.tree[i*2+2] = self.toggledValue[i*2+2][self.tracted[i*2+2] %2]
            self.tracted[i]  =0
            
    def query(self, left, right):
        return self._query_util(left,right,0,self.n-1,0)
    
    # value must be in between the left and right
    def queryFirst_Max(self,left,right,value):
        if left == right:
            return left 
        mid = (left +right) >>1
        mxv = self.query(left,mid)
        if mxv == value:
            return self.queryFirst_Max(left,mid,value)
        else:
            return self.queryFirst_Max(mid+1,right,value)

    def _update_util(self, i, ln, rn, x, v):
        if x>=ln and x<=rn:
            if ln != rn:
                ## may need modify
                self._update_util( 2*i+1, ln, (ln+rn)//2, x, v )
                self._update_util( 2*i+2, (ln+rn)//2 + 1, rn, x, v )
                self.tree[i] = self.merge(self.tree[2*i+1], self.tree[2*i+2])
                ## update toggle Value
                self.toggledValue[i] = [self.tree[i], mod - self.tree[i]]
            else:
                self.tree[i] = self.basef(v)
                ## update toggle Value
                self.toggledValue[i] = [self.tree[i], mod - self.tree[i]]

    def updateTo(self, x, v):
        self._update_util( 0, 0, self.n-1, x, v )   
        self.array[x] =v 
    
    def updateRange(self,left,right,delta):
        self.__update(left,right,0,self.n-1,0,delta)
        
    def __pushUp(self,root):
        self.tree[root] = self.merge(self.tree[2*root+1],self.tree[2*root+2])       
        self.toggledValue[root] = [self.tree[root], mod - min(self.tree[2*root+1],self.tree[2*root+2])] 
        #self.lazy[root] = 0
        #self.tracted[root] =0

    def __update(self,L,R,l,r,root,delta):
        if L <=l <=r<=R:
            self.lazy[root] = True
            self.tracted[root] += delta
            ## need to change
            self.tree[root] =self.toggledValue[root][self.tracted[root] %2]
            return 
        self.__pushDown(root,l,r)
        mid = (l+r) >>1
        if L <= mid:
            self.__update(L,R,l,mid,2*root+1,delta)
        if R >= mid +1:
            self.__update(L,R,mid+1,r,2*root+2,delta)
        self.__pushUp(root)
            



def resolve():
    inp = int(input())
    ls = list(map(lambda x: int(x),input().split()))
    n = int(input()) 
    st= segment_tree(ls,max)
    ret = []
    for _ in range(n):
        l,r=tuple(map(lambda x: int(x),input().split())) 
        print(st.query(0,inp-1),st.query(0,0),"####",st.query(0,0),st.query(0,1),st.query(0,2))
        st.updateRange(l-1,r-1,1)
        mxv = st.query(0,inp-1)
        idx = st.queryFirst_Max(0,inp-1,mxv)
        print(idx,mxv,l,r,st.query(0,0),st.query(0,1),st.query(0,2))
        ret.append(idx)
    return -1

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)