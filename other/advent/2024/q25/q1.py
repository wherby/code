import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
f=open(filename,'r')
FILEDEBUG=False

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin




def readMap():
    ls = []
    for _ in range(7):
        a = input()
        a = [a for a in a]
        ls.append(a)
    input()
    return ls

def isLock(ls):
    return all([a =="#" for a in ls[0]] )

def readKey(ls):
    ret = [0]*5
    #print(ls)
    for i in range(5):
        s= 0
        while ls[s+1][i]=="#":
            s +=1
        ret[i] =s 
    return ret

def solve():
    lss = []
    for _ in range(500):
        lss.append(readMap())
    lks,ks = [],[]
    for ls in lss:
        if isLock(ls):
            lks.append(readKey(ls))
        else:
            ls = ls[::-1]
            ks.append(readKey(ls))
    acc = 0
    for lk in lks:
        for k1 in ks:
            t = [a+b for a,b in zip(lk,k1)]
            if all([a<=5 for a in t]):
                acc +=1
    print(acc)
    
    

if FILEDEBUG:
    import sys

    orig_stdout = sys.stdout
    f = open('./.tmp/out2.txt', 'w')
    sys.stdout = f

solve()

if FILEDEBUG:
    sys.stdout = orig_stdout
    f.close()
    