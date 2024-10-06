# 
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/substitution_cipher_validation_input.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin


from functools import cache
MOD =  998244353

def resolve():
    ls = input().split()
    N = int(ls[1])
    s1 = [a for a in ls[0]]
    n = len(s1)
    ls = [] 
    for i,a in enumerate(s1):
        if a == "?":
            if i ==n-1 and i>0 and (s1[i-1]=="?" or  (s1[i-1]!= "?" and (int(s1[i-1])>2 or int(s1[i-1]) ==0 ))  ):
                s1[i] ="9"
            if i==n-1 or (s1[i+1] != "?" and  int(s1[i+1])<7) or s1[i+1] == "?":
                ls.append(i)
            else:
                s1[i] ="1"
    t = len(ls)
    m = (1<<t)-N
    #print(m,ls,1<<t,N) 
    for i in range(len(ls)):
        if 1<<(t-1-i) <=m:
            s1[ls[i]]="2"
            m -=1<<(t-1-i)
        else:
            s1[ls[i]] ="1"
    cnt = 0 

    @cache
    def dfs(i):
        if i == n:
            return 1
        if int(s1[i]) ==0:
            return 0
        ret = 0
        ret =dfs(i+1)
        if i<n-1 and (int(s1[i])<=2 and int(s1[i])>0 and (int(s1[i+1]) + int(s1[i])*10 )<=26):
            ret += dfs(i+2)
        return ret
    acc = dfs(0)%MOD
    # print(acc)
    
    return "".join(s1) + " " + str(acc)

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)