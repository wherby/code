#https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a45ef7
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

import math
def isPalin(state,str1):
    n = len(str1)
    re =""
    for i in range(n):
        if state &(1<<i):
            re += str1[i]
    for i in range(len(re)):
        if re[i] != re[len(re)-1-i]:
            return False
    return True


def resolve():
    n= int(input())
    str1= input()
    mod = 10**9+7
    st =[[] for i in range(n)]
    for state in range((1<<n)-1):
        t = bin(state).count("1")
        st[t].append(state)
    st =[[isPalin(a,str1) for a in arr]  for arr in st]
    acc =[]
    for s1 in st:
        tr =s1.count(True)
        l = len(s1)
        k =math.gcd(tr,l)
        acc.append((tr//k,l//k))
    #print(acc)
    a,b =0,1
    for c,d in acc:
        b1 = b*d
        a1 = a*d + b*c
        k = math.gcd(a1,b1)
        a,b =a1 //k ,b1//k
    #print(a,b)
    for i in range(a*b):
        if (i*mod +a) %b ==0:
            return (i*mod+a)//b
        # if i >10**5:
        #     return i

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)