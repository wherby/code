#https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4672b
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



def getState(state,allls):
    ls = []
    for a in allls:
        t = state %2 
        state = state //2
        if t:
            ls.append(a)
    return ls

def resolve():
    inp = int(input())
    seed = [i for i in range(1,inp+1)]
    seed = [5,1,3]
    ts =[str(x) for x in seed]
    ts= " ".join(ts)
    print(ts)
    ls2 = list(map(lambda x: int(x),input().split()))
    allls = seed +ls2
    sm  = sum(allls)
    for i in range(2<<(inp*2)):
        state = i
        ls = getState(state,allls)
        #print(ls)
        #print(len(ls), sum(ls),sm)
        if len(ls) == inp and sum(ls) *2 ==sm:
            ts =[str(x) for x in ls]
            print(" ".join(ts))
            break 

def op(caseidx):
    resolve()

for i in range(int(input())):
    op(i)