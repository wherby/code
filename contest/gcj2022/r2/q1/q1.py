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


def getIdx(x,mid):
    cir = x //8
    remder = x%8
    if remder ==6:
        return [(mid-cir-1,mid),(mid-cir,mid)]
    elif remder == 4:
        return [(mid,mid+cir+1),(mid,mid+cir)]
    elif remder ==2:
        return [(mid+cir+1,mid),(mid+cir,mid)]
    elif remder ==0:
        return [(mid,mid-cir-1),(mid,mid-cir)]

def getRealIdex(x,y,n):
    t = (x,y,n)
    acc =0
    while x!=1 and y !=1 and x != n and y!=n:
        x -=1
        y -=1
        acc += (n-1)*4
        n -=2
    #print(acc,x,y,n)
    if x ==y:
        return acc+1
    if x ==1:
        acc += ((n+1)//2)
    if y == n:
        acc +=((n+1)//2) + n-1
    if x ==n:
        acc += ((n+1)//2) + (n-1) *2
    if y ==1:
        acc += ((n+1)//2) + (n-1) *3
    return acc
        

def resolve(caseidx):
    ls = input().split(" ")
    ls = [int(x) for x in ls]
    n,k = ls[0],ls[1]
    m = n-1
    remain = n*n-1 -k 
    if remain %2 ==1 or k <m:
        return print("Case #"+str(caseidx+1)+": " + "IMPOSSIBLE")
    res = []
    idx = (n-1)//2
    while remain >0 and idx >0:
        if remain >= idx *8-2:
            remain -= idx*8-2
            res.append(idx*8-2)
        else:
            if remain >0:
                res.append(remain)
                remain =0
        idx -=1
    ret = []
    for t in res:
        s,e = getIdx(t,(n+1)//2)
        ret.append((getRealIdex(s[0],s[1],n),getRealIdex(e[0],e[1],n)))
    print("Case #"+str(caseidx+1)+": " + str(len(ret)))
    for a,b in ret:
        #print(a)
        print(str(a) + " " +str(b))
        
    
    

def op(caseidx):
    ret= resolve(caseidx)
    # if len(ret) ==0:
    #     print("Case #"+str(caseidx+1)+": " + "IMPOSSIBLE")
    # else:
    #     print("Case #"+str(caseidx+1)+": " + str(len(ret)))
    #     for a,b in ret:
    #         #print(a)
    #         print(str(a) + " " +str(b))
    

for i in range(int(input())):
    op(i)
    

# 2 4 6
# 8 10 12 14