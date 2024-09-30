def resolve():
    isG = False
    N,K = list(map(lambda x: int(x),input().split()))
    ls =[]
    for i in range(N):
        inp = int(input())
        ls.append(inp)
    mn = min(ls)
    if K >= mn*(2* max((N-1),1)-1):
        isG = True
    if isG:
        return "YES"
    else:
        return "NO"

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)