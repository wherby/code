# 
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/cottontail_climb_part_2_input.txt"
#filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin



from functools import cache
from collections import defaultdict,deque
@cache
def dfs(idx,m):
    if m <1 and idx >=0:
        return []
    if idx<0 :
        return [""]
    ret = []
    for i in range(1,m+1):
        a = [str(i) + b  for b in dfs(idx-1,i)]
        ret.extend(a)
    return ret

@cache
def getNstr(m):
    ret=[]
    for i in range(1,10):
        a = [str(i) + b for b in dfs(m-1,i-1)]
        ret.extend(a)
    return ret
    

def resolve():
    A,B,M = list(map(lambda x: int(x),input().split()))
    cnt = 0
    T= (len(str(B))+1)//2
    
    for i in range(T):
        
        ls1 = getNstr(i)
        dic = defaultdict(list)
        for a in ls1:
            t = int(a)%M
            dic[t].append(a)
        visit ={}
        for b in ls1:
            c = b[1:][::-1]
            #print(c,b,"a",ls1)
            if c not in visit:
                visit[c] =1 
            else:
                continue
            if len(c)>0:
                t1 = (M-int(c)*(10**len(b))) %M
            else:
                t1 = (M-0)%M
            #print("aa",b)
            for b1 in dic[t1]:
                if len(c)>0 and int(c[-1]) >=  int(b1[0]):
                    #print(b1,c)
                    continue
                d = int(c + b1)
                if A<=d <=B:
                    #print(d)
                    cnt +=1

    return cnt

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)