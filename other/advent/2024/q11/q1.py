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


def solve():
    ls= input()
    ls = list(map(int, ls.split(" ")))
    for _ in range(25):
        tmp =[]
        for a in ls:
            
            if a ==0:
                tmp.append(1)
            elif len(str(a)) %2 ==0:
                s = str(a)
                m = len(s)
                tmp.append(int(s[:m//2]))
                tmp.append(int(s[m//2:]))
            else:
                tmp.append(a*2024)
        ls=tmp
    print(len(ls))
    #print(ls[:100])


solve()