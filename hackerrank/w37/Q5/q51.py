filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)

mem ={}

def verifyLs(ls,dic):
    for i in ls:
        if dic[i] != 1:
            return False
    return True

def getValue(dic):
    global vls
    res =0
    for ls in vls:
        lst, value = ls
        if verifyLs(lst,dic):
            res = res + value
    return res

def getAllValue(dic1,dic2):
    return getValue(dic1) + getValue(dic2)


def tryMoveOne(dic1,dic2, t):
    dic1[t] =0
    dic2[t] =1
    tempMax = getAllValue(dic1,dic2)
    dic1[t] =1
    dic2[t] =0
    return (t,tempMax)

def moveOneToAnother(dic1,dic2):
    global n
    if sum(dic1[1:n+1]) ==1:
        return
    indexls =[]
    for i in range(1,n+1):
        if dic1[i] ==1:
            indexls.append(i)
    MMX =getAllValue(dic1,dic2)
    tx = 0
    for i in indexls:
        t,tempMax = tryMoveOne(dic1,dic2,i)
        if tempMax > MMX:
            MMX = tempMax
            tx = t 
    if tx != 0:
        dic1[tx] =0
        dic2[tx] =1


def getKeys(dic1):
    global n
    keys = []
    for i in range(1,n+1):
        if dic1[i] ==1:
            keys.append(i)
    return tuple(keys)

def getTempMax(dic1,dic2):
    global mem,n
    if getKeys(dic1) in mem:
        return mem[getKeys(dic1)]
    keys = []
    MAXT1 = getAllValue(dic1,dic2)
    moveOneToAnother(dic1,dic2)
    moveOneToAnother(dic2,dic1)
    CCMAX = getAllValue(dic1,dic2)
    while MAXT1 != CCMAX:
        MAXT1 = getAllValue(dic1,dic2)
        moveOneToAnother(dic1,dic2)
        moveOneToAnother(dic2,dic1)
        CCMAX = getAllValue(dic1,dic2)
        keys.append(getKeys(dic1))
    for key in keys:
        mem[key] = CCMAX
    return CCMAX

def getALLUnion(vls,n):
    ls =[-1] *50
    cnt = 1
    for ls1 in vls:
        tls ,value = ls1
        k = cnt
        for i in tls:
            if ls[i] != -1:
                cnt = min(cnt, ls[i])
        for i in tls:
            if ls[i] ==-1:
                ls[i] = cnt
            else:
                j = ls[i]
                for k in range(50):
                    if ls[k] == j:
                        ls[k] = cnt 
        cnt = cnt +1
    ls = filter(lambda x: x == 1,ls)
    if len(ls) == n:
        return True
    else:
        return False

def getALLVLS(vls):
    cnt =0
    for ls1 in vls:
        tls,value =ls1
        cnt = cnt +value
    return cnt

n,m = map(int , ins[0].strip().split())

vls =[]
index=1
for i in range(m):
    ls1= map(int , ins[index+i*2].strip().split())
    ls2= map(int , ins[index+i*2 +1].strip().split())
    vls.append([ls2,ls1[1]])
dic1 = [0]*50
dic2 = [0]*50
ALLMAXT =0
for i in range(1,n+1):
    dic1 = [1] *50
    dic2 = [0]*50
    dic1[i] =0
    dic2[1] =1
    MAXT = getAllValue(dic1,dic2)
    TMAX = getTempMax(dic1,dic2)
    if TMAX > ALLMAXT:
        ALLMAXT =TMAX
for i in range(1,n+1):
    for j in range(i+1,n+1):
        dic1 = [1] *50
        dic2 = [0]*50
        dic1[i] =0
        dic1[j] =0
        dic2[i] = 0
        dic2[j] =0
        MAXT = getAllValue(dic1,dic2)
        TMAX = getTempMax(dic1,dic2)
        if TMAX > ALLMAXT:
            ALLMAXT =TMAX


if not getALLUnion(vls,n):
    print getALLVLS(vls)
else:
    print ALLMAXT


