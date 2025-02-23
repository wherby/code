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
    ls = input()
    print(len(ls))
    n = len(ls)
    ls = [int(a) for a in ls]
    sm = sum(ls)
    print(sm)
    tls = [-1]*sm
    cur=0
    ls1,ls2 =[],[]
    for i in range(n):
        if i%2 ==0:
            ls1.append((cur,cur+ ls[i]-1))
            for j in range(ls[i]):
                tls[cur] = i//2
                cur +=1
        else:
            ls2.append((cur,cur+ls[i]-1))
            for j in range(ls[i]) :
                cur +=1
   # print(ls1,ls2)
    m = len(ls1)
    for i in range(m-1,1,-1):
        a = ls1[i][1] -ls1[i][0]+1
        for j in range(i):
            b = ls2[j][1] + 1 - ls2[j][0]
            if a <=b:
                
                for k in range(a):
                    tls[ls2[j][0] +k] = i
                ls2[j] = (ls2[j][0] +a,ls2[j][1])
                for k in range(a):
                    tls[ls1[i][0] + k] = -1
                break

    acc =0
    #print(tls)
    for i,a in enumerate(tls):
        if a >=0:
            acc += i*a 
    print(acc)

    


solve()