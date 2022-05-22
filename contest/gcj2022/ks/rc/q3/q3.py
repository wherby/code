#https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4621b
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




from collections import deque
def resolve():
    ls =list(map(lambda x: int(x),input().split()))
    n,L = ls[0],ls[1]
    ant=[]
    hp=[]
    for i in range(n):
        p,d = tuple(list(map(lambda x: int(x),input().split())))
        ant.append([p,i+1,d])
    pp =[]
    ant.sort()
    for p,idx,d in ant:
        pp.append(idx)
        if d ==0:
            hp.append((p,d))
        else:
            hp.append((L-p,d))
    hp.sort()
    dq = deque(pp)
    res =[]
    st =deque(hp)
    while st:
        p,d = st.popleft()
        if st and p == st[0][0]:
            _,d = st.popleft()
            x,y = dq.pop(),dq.popleft()
            res.append(min(x,y))
            res.append(max(x,y))
        else:
            if d ==0:
                res.append(dq.popleft())
            else:
                res.append(dq.pop())
    
    return res
def op(caseidx):
    ret= resolve()
    ret = list(map(lambda x:str(x),ret))
    print("Case #"+str(caseidx+1)+": "+" ".join(ret) )
    

for i in range(int(input())):
    op(i)