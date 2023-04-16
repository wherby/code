# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b94/0000000000cad9c1
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



def verif(inp,idx):
    return (idx+1)*idx //2 *26 <=inp

def resolve():
    inp = input()
    n = len(inp)
    isG =True
    for i in range(n-1):
        #print(i,inp,n,inp[i],inp[i+1])
        if inp[i] != inp[i + 1]:
            isG =False
    if isG==True:
        if n ==1:
            return 0
        return (n+1)//2
    inp = inp*2
    #print(inp,n)
    for i in range(n):
        if inp[i] != inp[i+1]:
            inp = inp[i+1:i+1+n]
            break
    idx = 0 
    cnt =0
    #print(inp)
    while idx < n:
        if idx < n-1 and inp[idx] ==inp[idx+1]:
            cnt +=1
            idx +=2
        else:
            idx +=1
    return cnt

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)