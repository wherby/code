def resolve():
    N,G = list(map(lambda x: int(x),input().split()))
    ls =[]
    for i in range(N):
        inp = int(input())
        ls.append(inp)
    ret = 0
    ls.sort()
    mx = abs(G - ls[0])
    for i ,a in enumerate(ls):
        d =abs(G-a)
        if d <= mx:
            mx = d 
            ret = i 

    return str(N-ret) + " " + str(mx)

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)