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


def debugmp(cx,cy):
    return
    mp[cx][cy] ="@"
    # for a in mp:
    #     print(a)
    mp[cx][cy]="."

mp =[]

s1 = set(["[","]"])
def move(cx,cy,dx,dy):
    if mp[cx+dx][cy+dy] ==".":
        return (cx+dx,cy+dy)
    elif mp[cx+dx][cy+dy] =="#":
        return (cx,cy)
    else:
        #print("aaaa",cx,cy,dx,dy)
        #debugmp(cx,cy)
        ccx,ccy =cx,cy
        ls = []
        if  mp[cx+dx][cy+dy] =="[":
            ls.append([(cx+dx,cy+dy),(cx+dx,cy+dy+1)])
        else:
            ls.append([(cx+dx,cy+dy-1),(cx+dx,cy+dy)])
        #print(ls)
        tls = ls[-1]
        goodToMV = True
        while (not all([mp[x][y] == "." for x,y in tls])) or (not any([mp[x][y] == "#" for x,y in tls])) and len(tls)>0 and goodToMV:
            tmp= set([])
            for x,y in tls:
                if mp[x+dx][y+dy] =="[" and(mp[x][y] in s1):
                    tmp.add((x+dx,y+dy))
                    tmp.add((x+dx,y+dy+1))
                elif mp[x+dx][y+dy] =="]" and(mp[x][y] in s1):
                    tmp.add((x+dx,y+dy-1))
                    tmp.add((x+dx,y+dy))
                elif (mp[x][y] in s1) and mp[x+dx][y+dy] ==".":
                    pass
                elif  (mp[x][y] in s1) and mp[x+dx][y+dy] =="#":
                    goodToMV = False
            tls = list(tmp)
            if len(tls)>0:
                ls.append(tls)
        #print("*"*100)
        #print(ls)
        if all([mp[x][y] == "."  for x,y in tls])  and goodToMV:
            #print(tls)
            while len(ls):
                tls = ls.pop()
                for x,y in tls:
                    mp[x+dx][y+dy] = mp[x][y]
                    mp[x][y ] ="."

            
            return (ccx+dx,ccy+dy)
        else:
            return (ccx,ccy)
        
def move2(cx,cy,dx,dy):
    # print("aaaa",cx,cy,dx,dy)
    # for a in mp:
    #     print(a)
    if mp[cx+dx][cy+dy] ==".":
        return (cx+dx,cy+dy)
    elif mp[cx+dx][cy+dy] =="#":
        return (cx,cy)
    else:
        ccx,ccy =cx,cy
        
        while mp[cx+dx][cy+dy] =="[" or mp[cx+dx][cy+dy] =="]"  :
            cx,cy =cx+dx,cy+dy
        if mp[cx+dx][cy+dy] == ".":
            while cx !=ccx or cy !=ccy:
                #print(cx,dx,cy,dy,mp[cx][dx])
                mp[cx+dx][cy+dy] = mp[cx][cy]

                cx,cy = cx-dx,cy-dy
            mp[ccx+dx][ccy+dy] ="."
            return (ccx+dx,ccy+dy)
        else:
            return (ccx,ccy)

def solve():
    mp2=[]
    a = input()
    while len(a)>1:
        mp2.append(a)
        a = input()

    for a1 in mp2:
        tmp =[]
        for b1 in a1:
            if b1 =="#":
                tmp.append("##")
            if b1 =="O":
                tmp.append("[]")
            if b1==".":
                tmp.append("..")
            if b1 =="@":
                tmp.append("@.")
        tmp ="".join(tmp)
        #print(tmp)
        tmp=[a for a in tmp]
        mp.append(tmp)

    
    mvs =[]
    a = input()
    while len(a)>1:
        mvs.append(a)
        a = input()
    mvs ="".join(mvs)
    dirs ={"v":(1,0),"<":(0,-1),">":(0,1),"^":(-1,0)}
    m,n = len(mp),len(mp[0])
    for i in range(m):
        print(mp[i])
    cx,cy =-1,-1
    for i in range(m):
        for j in range(n):
            if mp[i][j] =="@":
                cx,cy = i,j 
                mp[i][j] ="."
    for m1 in mvs:
        dx,dy =dirs[m1]
        #print(m1,"beformv")
        #debugmp(cx,cy)
        if dx ==0:
            cx,cy =move2(cx,cy,dx,dy)
        else:
            cx,cy = move(cx,cy,dx,dy)
        #print("afer mv "  + "()*"*100)
        #debugmp(cx,cy)

    acc =0
    for i in range(m):
        for j in range(n):
            if mp[i][j] =="[":
                acc += i*100+j 
    print(acc)
    
    
    
import sys

orig_stdout = sys.stdout
f = open('./.tmp/out2.txt', 'w')
sys.stdout = f

solve()
sys.stdout = orig_stdout
f.close()