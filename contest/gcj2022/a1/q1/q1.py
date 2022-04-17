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



def resolve():
    str1 = input().split()[0]
    n = len(str1)
    last = str1[-1]
    res =[last]
    last =str1[-1]
    state = False
    for i in range(n-2,-1,-1):
        a = str1[i]
        if a < last:
            res.append(a)
            res.append(a)
            state = True
            last =a
        elif a == last and state ==True:
            res.append(a)
            res.append(a)
        else:
            res.append(a)
            last =a
            state = False
    res.reverse()
    ret ="".join(list(res))
    return ret
    

def op(caseidx):
    ret= resolve()
    print("Case #"+str(caseidx+1)+": " + ret)
    

for i in range(int(input())):
    op(i)