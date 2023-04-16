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
    n = int(input())
    ls = input().split(" ")
    dic ={}
    rdic={}
    cur = 0
    lst = -1
    for a in ls:
        if a not in dic:
            dic[a] = cur
            rdic[cur] =a
            lst =cur 
            cur +=1
        else:
            if a != rdic[lst]:
                return "IMPOSSIBLE"
    ret =[]
    #print(dic)
    for i in range(cur):
        ret.append(rdic[i])
    return " ".join(ret)
            

    

def op(caseidx):
    ret= resolve()
    print("Case #"+str(caseidx+1)+": " +ret )
    

for i in range(int(input())):
    op(i)