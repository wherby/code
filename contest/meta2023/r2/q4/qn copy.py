#https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/wiki_race_input.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin


from collections import defaultdict,deque
import sys
sys.setrecursionlimit(10000000)

def resolve():
    n = int(input())
    g = [[] for _ in range(n)]
    lss = list(map(lambda x: int(x),input().split()))
    ind = [0]*n
    for i,a in enumerate(lss,1):
        g[a-1].append(i)
        ind[a-1]+=1
    
    cnt = 0
    sst = [[] for _ in range(n)]
    for i in range(n):
        tls = input().split()
        sst[i] = set(tls[1:])
    cand = []
    for i in range(n):
        if ind[i] == 0 :
            cand.append(i)
    leves = len(cand)
    
    st = [0]
    while st:
        i = st.pop()
        if len(g[i]) ==1:
            b = g[i][0]
            for c in sst[b]:
                sst[i].add(c)
            sst[b] = []
            g[i] = g[b]
            st.append(i)
        else:
            for b in g[i]:
                st.append(b)
    
    # def dfs(i):
    #     for b in g[i]:
    #         dfs(b)
    #     if len(g[i]) ==1:
    #         b = g[i][0]
    #         for c in sst[b]:
    #             sst[i].add(c)
    #         sst[b] = []
    #         g[i] = g[b]
    # dfs(0)
    dc = defaultdict(int)
    for ls in sst:
        for a in ls:
            dc[a] +=1

    def verify(i,word):
        acc= word in sst[i]
        for a in g[i]:
            acc+= verify(a,word)
        if acc < len(g[i]) and len(g[i])>1:
            return -10**10
        #print(i,word,acc,len(g[i]),acc < len(g[i]))
        return acc if acc<=1 else 1
    #isG = True
    #print(leves)
    for k,v in dc.items():
        if v >=leves:
            #print(k)
            #print(verify(0,k))
            if verify(0,k) >=0 :
                cnt +=1
                #print(k)
    #print(leves)
    return cnt

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)