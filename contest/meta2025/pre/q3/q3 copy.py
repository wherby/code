


def resolve():
    n = int(input())
    ls = list(map(lambda x: int(x),input().split()))
    cur =0 
    cmx = 0
    tmp = []
    lss=[]
    while cur < n:
        a = ls[cur]
        if cmx ==0:
            cmx = a 
            tmp.append(a)
            cur +=1
        elif a ==cmx+1:
            cmx = a 
            tmp.append(a)
            cur +=1
        else:
            d= cmx -len(tmp)
            tmp.extend(ls[cur:cur+d])
            cur = cur+d
            lss.append(list(tmp))
            tmp = []
            cmx=0
    if tmp:
        lss.append(tmp)
    ret = []
    acc = 0
    cnt =0
    for b in lss[::-1]:
        d = len(b)
        e = (b[0]-1 -acc)%d
        acc +=e 
        ret.append((d,e))
        cnt +=1
        cnt +=e
    
    return (cnt, ret[::-1])

def op(caseidx):
    cnt,ret = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))
    for a,b in ret:
        print("1",a)
        for _ in range(b):
            print("2")

for i in range(int(input())):
    op(i)