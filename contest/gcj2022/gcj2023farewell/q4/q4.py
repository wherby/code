#https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a45ef7
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
    inp = int(input())
    inp -=1
    l,r =0,10**8
    while l<r:
        mid = (l+r)>>1
        if verif(inp,mid):
            l = mid+1
        else:
            r = mid
    inp = inp - (l-1)*l //2*26
    inp = inp //l 
    #print(inp,l)
    return chr(ord("A")+inp)

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)