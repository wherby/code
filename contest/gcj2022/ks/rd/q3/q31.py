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


# Will work in pypy

from collections import defaultdict,deque
from bisect import bisect_left
def resolve():
    m, = tuple(list(map(lambda x: int(x),input().split())))
    ls2  = list(map(lambda x: int(x),input().split()))
    n, =  tuple(list(map(lambda x: int(x),input().split())))
    ls1 = list(map(lambda x: int(x),input().split()))
    kls= [ls2[0]]
    for i in range(1,m):
        if ls2[i] == kls[-1]:continue
        kls.append(ls2[i])
    m = len(kls)
    lls =[[] for _ in range(2501)]
    for i,a in enumerate(ls1):
        lls[a].append(i)
    st =deque([])
    for a in lls[kls[0]]:
        st.append((0,a,0))
    #print(kls)
    visited ={}
    mx = 10**19
    while st:
        #print(st)
        cost,a,idx = st.popleft()
        if (a,idx) in visited and cost > visited[(a,idx)]:continue
        if idx ==m-1:
            mx = min(mx,cost)
            continue
        b = kls[idx+1]
        bidx = bisect_left(lls[b],a)
        if bidx>0:
            if (lls[b][bidx-1],idx+1) not in visited or visited[(lls[b][bidx-1],idx+1)] > cost + abs(lls[b][bidx-1]-a) :
                st.append((cost + abs(lls[b][bidx-1]-a),lls[b][bidx-1],idx+1))
                visited[(lls[b][bidx-1],idx+1)] =cost + abs(lls[b][bidx-1]-a)
        if bidx < len(lls[b]):
            if (lls[b][bidx],idx +1) not in visited or visited[(lls[b][bidx],idx +1)] >cost +abs(lls[b][bidx]-a):
                st.append((cost +abs(lls[b][bidx]-a),lls[b][bidx],idx +1))
                visited[(lls[b][bidx],idx +1)] =cost +abs(lls[b][bidx]-a)
    return str(mx)
    
    
    
def op(caseidx):
    ret= resolve()
    print("Case #"+str(caseidx+1)+": " + ret)
    

for i in range(int(input())):
    op(i)