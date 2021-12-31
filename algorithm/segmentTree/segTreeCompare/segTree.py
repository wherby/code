class SegTree:
    def __init__(self,n):
        self.c = [0]*(n *4)
        self.n = n *4
    
    def add(self,x,count):
        while x <= self.n:
            self.c[x] +=count
            x += x & -x
    
    def ask(self,x):
        ans = 0 
        while x:
            ans += self.c[x]
            x -= x & -x
        return ans
    def reset(self):
        self.c = [0]*self.n


st = SegTree(1000)
ls =[3,2,4,5,1]
n = len(ls)
r,l = [0]*n ,[0]*n
for i in range(n-1,-1,-1):
    r[i] = st.ask(ls[i] -1)
    st.add(ls[i],1)
st.reset()
for i in range(n):
    l[i] = st.ask(ls[i]-1)
    st.add(ls[i],1)
print(l,r)