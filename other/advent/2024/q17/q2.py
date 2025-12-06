import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
f=open(filename,'r')
FILEDEBUG=True

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
        return 

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
    cpy = ops.strip()
    #print(cpy)
    # for i in range(1,1000):
    #     re =getD(i,A,B,C,ops)
    #     print(i,re)
    #     if re ==cpy:
    #         print(i)
    D13= 8**13
    D12= 8**12
    D11= 8**11
    D10= 8**10
    D9=8**9
    D8=8**8
    D6=8**6
    start =8796093022208*4
    
    # for i in range(start, start + 8**8):
    #     re =getD(i,A,B,C,ops)
    #     #print(i,re)
    #     if re ==cpy:
    #         print(i)
    #         print("."*100)
    print("aaa")
    # want= "4,0,1,7,5,5,3,0"
    # for i in range(8*8):
    #     for j in range(64*8):
    #         re =getD(start*7 +start//2*1 + D13*3 + D12*1+D11*3+D10*6+D9*5+i*D8+j,A,B,C,ops)
    #         #print(re,i)
    #         print(re[16:],want)
            
    #         if re[16:] == want:
    #             print(i)
    #             print(".,..")
    #         if re == cpy:
    #             print(re,i)
    D15 = 8**14
    D3 =8**3
    start = D15*58 + D12 *48 +D9*72 +D6*24 +D6*314 +D3*401
    for i in range(-512*64,512*64):
        re =getD(start +i,A,B,C,ops)
        #print(len(re) , " ", i,len(cpy))
        #print(re[-23:])
        #print(re[10:])
        #print(re[-7:])
        #print(re[-11:])
        b ="2,4,1,7,7,5,0,3,4,0,1,7,5,5,3,0"
        bl =len(b)
        if re[-bl:]==b and len(re) == len("2,4,1,7,7,5,0,3,4,0,1,7,5,5,3,0"):
            print(re,i)
    print("*"*100)
    print(start +411)

def getD(D, a,b,c,ops):
    global A,B,C,outls
    A,B,C =a,b,c 
    outls =[]
    
    
    ops = ops.split(",")
    ops = [int(a) for a in ops]
    #print(ops)  
    n = len(ops)
    cur = 0
    A = D
    #print(A,B,C,ops,cur)

    while cur != n:
        
        a = ops[cur]
        op = ops[cur +1]
        #print(cur,a,op,A,B,C, "       start")
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
        #print(cur,a,op,A,B,C)
    outls = [str(a) for a in outls]
    result =",".join(outls)
    #print(",".join(outls))
    return result 

    

if FILEDEBUG:
    import sys

    orig_stdout = sys.stdout
    f = open('./.tmp/out2.txt', 'w')
    sys.stdout = f

solve()

if FILEDEBUG:
    sys.stdout = orig_stdout
    f.close()

print(8**14*2)
print(8**3)