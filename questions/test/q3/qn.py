#https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c
#https://www.techinfodiaries.com/reversort-engineering-solution-codejam/
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


def create(n):
    h=[]
    for i in range(1,n+1):
        h.append(i)
    return h

def op2(n,c):
    if c<n-1:
        return[]
    h=[]
    a=0
    b=1
    for i in range(n-1,0,-1):
        b+=1
        if(a+b+i-1>=c):
            e=c-a-i+1
            h.append(e)
            for k in range(i-1):
                h.append(1)
            a=c
            break

        a+=b
        h.append(b)
    if(a<c):
        return []
    return h

def op1(h,h1):
    n=len(h1)
    for i in range(n):
        t=len(h)-(i+2)
        s=t+h1[i]
        h=h[:t]+list(reversed(h[t:s]))+h[s:]
    return h

def op():
    inp=input().split()
    n=int(inp[0])
    c=int(inp[1])
    h=create(n)
    h1=op2(n,c)
    print(h1)
    h=op1(h,h1)
    ans=""
    if h1:
        for item in h:
            ans+=str(item)+" "
    else:
        ans=" IMPOSSIBLE"
    print("Case #"+str(i+1)+": "+str(ans))

for i in range(int(input())):
    op()

