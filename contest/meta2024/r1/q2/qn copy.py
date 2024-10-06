


def get_prime(n):
    visited=[0]*(n+2)
    res =[]
    for i in range(2,n+1):
        if visited[i]: continue
        res.append(i)
        for j in range(i,n+1,i):
            visited[j] =1
    return res

def resolve():
    inp = int(input())
    pls = get_prime(inp)
    spls = set(pls)
    acc =1 
    if len(pls)<=2:
        return 0
    for a in pls:
        if a +2 in spls:
            acc +=1
    return acc

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)