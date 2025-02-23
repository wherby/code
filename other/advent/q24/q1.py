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



def getArray():
    ls=[]
    a = input()

    while len(a)>1:
        ls.append(a)
        a = input()
    return ls

def parser1(str1):
    ls = str1.split(":")
    ls = [a.strip() for a in ls]
    return (ls[0], int(ls[1]))

def parser2(str2):
    ls= str2.split(" ")
    #print(ls)
    return ls

def dfs(d):
    if d in visit:
        return visit[d]
    a,op,b = g[d]
    if op =="AND":
        return dfs(a) and dfs(b)
    if op =="OR":
        return dfs(a) or dfs(b)
    if op =="XOR":
        return dfs(a) ^ dfs(b)


visit={}
g ={}
def solve():
    ls1= getArray()
    ls2 = getArray()
    #print(ls1,ls2)
    
    for a in ls1:
        c,d= parser1(a)
        visit[c] = d 
    
    root=[]
    for a in ls2:
        ret = parser2(a)
        if ret[-1][0] =="z":
            root.append(ret[-1])
        g[ret[-1]] = ret[:3]

    root.sort(reverse= True)
    print(root)
    #print(g)
    ret= 0
    for a in root:
        ret =ret*2 + dfs(a)
    print(ret)

if FILEDEBUG:
    import sys

    orig_stdout = sys.stdout
    f = open('./.tmp/out2.txt', 'w')
    sys.stdout = f

solve()

if FILEDEBUG:
    sys.stdout = orig_stdout
    f.close()


# 1010110101101000110110010110010100101100000110 not correct