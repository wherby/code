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

def find(lss,tar):
    if len(lss) == 1:
        return lss[0] == tar

    ls = list(lss)
    a = ls.pop()
    b = ls.pop()
    ls.append(a+b)
    res = find(ls,tar)
    ls = list(lss)
    a = ls.pop()
    b = ls.pop()
    ls.append(a*b)
    res2= find(ls,tar)
    return res or res2

def solve():
    ls = []
    a = input()
    while len(a)>1:
        ls.append(a.split(" "))
        a = input()
    sm = 0
    for tl in ls:
        #print(tl,tl[0][:-1])
        tt =int(tl[0][:-1])
        t1 = tl[1:]
        t1= list(map(int, t1))
        t1= t1[::-1]
        if find(t1,tt):
            sm += tt
            #print(tt)
    print(sm)
    


solve()