import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
f=open(filename,'r')
from collections import defaultdict,deque
from collections import Counter
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin

def parse(s1):
    s1 =s1.split(" ")
    ret =[]
    for r1 in s1:
        r1= r1.split("=")[1]
        for a in r1.split(","):
            ret.append(int(a))
    return ret


def solve():
    ls = []
    a = input()
    while len(a)>1:
        print(a)
        a = parse(a)
        print(a)
        ls.append(a)
        a = input()
    A,B= 103,101
    ls1 = [0]*4
    #print(ls)
    import sys

    orig_stdout = sys.stdout
    f = open('./.tmp/out2.txt', 'w')
    sys.stdout = f

    for k in range(100000):
        tls= defaultdict(list)
        for y1,x1,dy,dx in ls:
            x = (x1+k*dx)%A
            y = (y1 + k*dy)%B 
            tls[x].append(y)
            if x==A//2 or y == B //2: continue
            a = int(x>A//2)
            b = int(y>B//2)
            c =a*2 +b 
            ls1[c] +=1
        
        sm = 0 
        for i in range(5):
            sm += len(tls[i])
        if sm < 10:
            print(str(k) + "  " + "*" *100)
            for i in range(101):
                tt = ["."]*101
                c = Counter(tls[i])
                for k,v in c.items():
                    tt[k] = str(v)
                tt = "".join(tt)
                print(tt)
    sys.stdout = orig_stdout
    f.close()

    acc = 1
    for a in ls1:
        acc=a*acc
    print(acc)

    


solve()