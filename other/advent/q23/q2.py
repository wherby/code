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





def solve():
    ls=[]
    a = input()

    while len(a)>1:
        a = a.split("-")
        ls.append(a)
        a = input()
    dic ={}
    keys =set([])
    for a,b in ls:
        dic[(a,b)] = 1
        dic[(b,a)] =1
        keys.add(a)
        keys.add(b)
    vs = {}
    for a,b in ls:
        for k in keys:
            if k != a and k !=b :
                if ((a,k) in dic)  and ((b,k) in dic) and (a,b) in dic:
                    #print((a,k) in dic, (b,k) in dic ,"*" *100)
                    #print(dic[(a,k)])
                    t = [a,b,k]
                    t.sort()
                    
                    t = tuple(t)
                    vs[t] =1
                    # isG = False
                    # for d in t:
                    #     if d[0]=="t":
                    #         isG =True
                    # if isG:
                    #     #print(((a,k) in dic) and ((b,k) in dic),a,k,b,((a,k) in dic))
                    #     #print(dic[(a,k)],dic[(b,k)],a,b,k)
                    #     vs[t] =1
    
    def growBigger(tss):
        ret =set([])
        for ts in tss:
            ts1 = set(ts)
            
            for k in keys:
                if k not in ts1 and all((k,a) in dic for a in ts):
                    #print(ts1,k)
                    tt=list(ts) +[k]
                    tt.sort()
                    tt= tuple(tt)
                    ret.add(tt)
        return ret
    tss = vs.keys()
    nss = growBigger(tss)
    while len(nss) >0:
        tss = nss 
        nss = growBigger(tss)
        # if len(list(nss)[0]) >3:
        #     print(len(nss))
        #     break
    print(tss)
    t111= list((list(tss))[0])
    print(",".join(t111))
        
    print(len(vs))

    

if FILEDEBUG:
    import sys

    orig_stdout = sys.stdout
    f = open('./.tmp/out2.txt', 'w')
    sys.stdout = f

solve()

if FILEDEBUG:
    sys.stdout = orig_stdout
    f.close()

# ay,bu,ci,ct,df,me,oi,py,sg,te,ur,wy not right