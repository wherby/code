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
from collections import defaultdict,deque

def solve():
    ls = []
    for _ in range(1176):
        ls.append(list(map(lambda x:int(x),input().split("|"))))
    fd = defaultdict(list)
    for a,b in ls:
        fd[a].append(b)
    ls2 = []
    input()
    for _ in range(205):
        ls2.append(list(map(lambda x:int(x),input().split(","))))
    ans = 0
    for tl in ls2:
        dic = {}
        isG = True
        for a in tl:
            for b in fd[a]:
                if b in dic:
                    isG = False
            dic[a] = 1 
        if isG:
            m = len(tl)
            ans += tl[m//2]
    return ans 
    


print(solve())