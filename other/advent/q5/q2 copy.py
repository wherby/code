import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input.txt"
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
    for _ in range(21):
        ls.append(list(map(lambda x:int(x),input().split("|"))))
    fd = defaultdict(list)
    for a,b in ls:
        fd[a].append(b)
    ls2 = []
    input()
    for _ in range(6):
        ls2.append(list(map(lambda x:int(x),input().split(","))))
    ans = 0
    for tl in ls2:
        dic = {}
        isG = True
        for i,a in enumerate(tl):
            for b in fd[a]:
                if b in dic:
                    print(tl,"a")
                    isG = False
                    tl[dic[b]],tl[i] = tl[i],tl[dic[b]]
                    dic[a] = dic[b]
                    dic[b] = i
            dic[tl[i]] = i 
        if not isG:
            while isG == False:
                isG = True
                dic ={}
                for i,a in enumerate(tl):
                    for b in fd[a]:
                        if b in dic:
                            print(tl,"a")
                            isG = False
                            tl[dic[b]],tl[i] = tl[i],tl[dic[b]]
                            dic[a] = dic[b]
                            dic[b] = i
                    dic[tl[i]] = i 
            m = len(tl)
            ans += tl[m//2]
    return ans 
    


print(solve())