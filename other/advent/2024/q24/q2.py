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
    print(d,"=", a, op,b)
    c1= dfs(a)
    c2= dfs(b)
    if op =="AND":
        visit[d] = c1 and c2
        return c1 and c2
    if op =="OR":
        visit[d] = c1 or c2
        return c1 or c2
    if op =="XOR":
        visit[d] = c1 ^c2
        return c1 ^c2


visit={}
g ={}
ls1= getArray()
ls2 = getArray()
cons = []
def solve():
    
    #print(ls1,ls2)
    xls,yls =[],[]
    for a in ls1:
        c,d= parser1(a)
        visit[c] = d
        if c[0]=="x":
            xls.append((c,d))
        else:
            yls.append((c,d))
    xls.sort(reverse=True)
    yls.sort(reverse=True)
    print(xls,yls)
    xacc=yacc =0
    for c,d in xls:
        xacc =xacc*2 +d 
    for c,d in yls:
        yacc =yacc*2 +d 
    print(xacc,yacc)
    
    root=[]
    
    for a in ls2:
        ret = parser2(a)
        if ret[-1][0] =="z":
            root.append(ret[-1])
        g[ret[-1]] = ret[:3]
        cons.append(ret)
    root.sort()
    for a in root:
        dfs(a)

    root.sort(reverse= True)
    #print(root)

    #print(g)
    
    
    def getValue():
        ret= 0
        for a in root:
            ret =ret*2 + dfs(a)
        #print(ret)
        return ret
    n = len(cons)
    print(bin(xacc))
    print(bin(yacc))
    z =getValue()
    print(bin(getValue()))
    #print(len(cons))
    print(xacc + yacc ==z)
    lss=  ["jst" ,"z05" , "mcm", "gdf","gwc" ,"z30","dnt","z15" ]
    lss.sort()
    print(",".join(lss))
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
# ["jst" <-> "z05" ,, "mcm"<-> "gdf","gwc" <->"z30" "dnt"<->"z15" ]
    
print(len("100011011100110"))