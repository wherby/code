filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys
from timeit import default_timer as timer

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)


#print ins

d1={}

n,m = map(int , ins[0].strip().split())
index=1
ls=[]
lsPick=[]
lsNotPick=[]
for i in range(m):
    a,b,c,d,= map(int , ins[index+i].strip().split())
    tls=[min(a,b),max(a,b),c,d]
    ls.append(tls)



def get(u):
    global col
    #return u
    if col[u] == u:
        return u
    a = get(col[u])
    return a

def join(u,v):
    global col,rk
    u = get(u)
    v = get(v)
    if u == v:
        return False
    if rk[u] > rk[v]:
        u,v = v,u
    rk[v] = rk[u] + rk[v]
    col[u] = v
    return True


def check(c):
    global ls,m,col,rk,A,B
    start = timer()
    ls.sort(key = lambda x: x[2] - c*x[3], reverse= True)
    
    #print index
    col = list(range(m))
    rk =[1]*m
    A =0
    B=0
    end = timer()
    #print(end - start)
    start = timer()
    for i in list(range(m)):
        if(join(ls[i][0],ls[i][1])):
            A = A + ls[i][2]
            B = B + ls[i][3]
    end = timer()
    #print(end - start)
    return A - B *c

left =0
right =1000.0

col =[]
rk=[]
A=0
B=0

for i in range(4):
    c = (left + right) /2
    start = timer()
    ls.sort(key = lambda x: x[2] - c*x[3], reverse= True)
    
    #print index
    col = list(range(m))
    rk =[1]*m
    A =0
    B=0
    end = timer()
    #print(end - start)
    start = timer()
    for i in range(m):
        if(join(ls[i][0],ls[i][1])):
            A = A + ls[i][2]
            B = B + ls[i][3]
    end = timer()
    print(end - start)
    
    re = A - B *c
    if abs(re)< 0.0001:
       break
    if re > 0:
        left = c
    else:
        right =c 

def gcd(a, b):
 if a < b:
  a, b = b, a
 while b != 0:
  temp = a % b
  a = b
  b = temp
 return a
#print A,B,ls
g = gcd(A,B)

print(str(A/g) +"/" + str(B/g))