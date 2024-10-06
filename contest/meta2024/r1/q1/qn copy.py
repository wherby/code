


def merge(a,b):
    if a[0]>b[0]:
        a,b = b,a 
    x1,y1 = a 
    x2,y2 = b 
    if y1 <x2:
        return []
    return [x2,min(y1,y2)]

def resolve():
    inp = int(input())
    tls =[]
    for i in range(1,inp+1):
        ls = list(map(lambda x: int(x),input().split()))
        tls.append([i/ls[1],i/ls[0] if ls[0] !=0 else 10**10])
    acc = tls[0] 
    for a in tls:
        acc = merge(a,acc)
        if len(acc) ==0:
            return -1
    
    return acc[0]

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)