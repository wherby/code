

def resolve():
    ls1 = list(map(lambda x: int(x),input().split()))
    ls2 = list(map(lambda x: int(x),input().split()))
    ls = [(b,a,i) for i,(a,b) in enumerate(zip(ls1,ls2),1)]
    ls.sort(reverse=True)
    cnt = 0
    dic ={}
    tls = []
    for b,a,i in ls:
        if b<a:
            return (-1,[])
        elif b ==a :
            pass
        elif b not in dic:
            return (-1,[])
        else:
            cnt +=1
            tls.append([i,dic[b]])     
        dic[a] = i
    tls=tls[::-1]
    return (cnt,tls)


def op(caseidx):
    cnt,tls = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))
    for a,b in tls:
        print(b,a)


for i in range(int(input())):
    op(i)