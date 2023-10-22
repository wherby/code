#https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/meta_game_input.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin



def resolve():
    inp = int(input())
    Als = list(map(lambda x: int(x),input().split()))
    Bls = list(map(lambda x: int(x),input().split()))
    for i in range(inp):
        Als.append(Bls[i])
        Bls.append(Als[i])
    for i in range(inp):
        Als.append(Als[i])
        Bls.append(Bls[i])
    isOdd = inp%2==1
    hf = inp //2
    for i in range(inp*2):
        if Als[i]< Bls[i] and Als[i+hf -1] < Bls[i+hf-1] and Als[i+hf+isOdd] > Bls[i+hf + isOdd] and Als[i+inp-1] > Bls[i+inp-1]:
            if isOdd:
                if Als[i+hf] != Bls[i+hf]:
                    return -1
            for j in range(hf):
                if Als[i+j] < Bls[i+j] and Als[i+j] == Bls[i+inp-1-j]:
                    continue
                else:
                    return -1
            return i      
    return -1

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)