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

A= -1
B= -1
C= -1

def getComb(v):
    global A,B,C
    if 0<=v<=3:
        return v
    if v ==4:
        return A 
    if v ==5:
        return B 
    if v ==6:
        return C 
    if v ==7:
        print("invalid")
        return -1

def adv(op):
    global A 
    res= A//(2** getComb(op))
    return res

def bxl(op):
    global B
    res= B^op
    B =res

def bst(op):
    global B
    B =getComb(op) %8 

def jnz(op):
    global A 
    if A ==0:
        return -1
    else:
        return op 

def bxc(op):
    global B,C 
    B=B^C 

outls = []
def out1(op):
    outls.append(getComb(op)%8)





def solve():
    global A,B,C,outls
    ls = []
    for _ in range(5):
        ls.append(input())
    lss = []

    for i in range(3):
        #print(ls[i])
        f =ls[i].split(":")[1]
        
        lss.append(int(f))
    A,B,C = lss[0],lss[1],lss[2]
    ops = ls[4].split(":")[1]
    ops = ops.split(",")
    ops = [int(a) for a in ops]
    print(ops)    
    n = len(ops)
    cur = 0

    while cur != n:
        
        a = ops[cur]
        op = ops[cur +1]
        print(cur,a,op,A,B,C, "       start")
        if a!=3:
            cur +=2
        else:
            t= jnz(op)
            if t == -1:
                cur +=2
            else:
                cur =t
        if a == 0:
            A= adv(op)
        if a ==1:
            bxl(op)
        if a ==2:
            bst(op)
        if a ==4:
            bxc(op)
        if a ==5:
            out1(op)
        if a ==6:
            B = adv(op)
        if a ==7:
            C = adv(op)
        print(cur,a,op,A,B,C)
    outls = [str(a) for a in outls]
    print(",".join(outls))

    

if FILEDEBUG:
    import sys

    orig_stdout = sys.stdout
    f = open('./.tmp/out2.txt', 'w')
    sys.stdout = f

solve()

if FILEDEBUG:
    sys.stdout = orig_stdout
    f.close()