


def resolve():
    isG = False
    N,M = list(map(lambda x: int(x),input().split()))
    if N < M :
        return "NO"
    if N >= 2*M+2:
        if N%2 == 1:
            return "NO"
        else:
            return "YES"
    for i in range(M,M+3):
        res = N-i
        #print(N,i,res)
        if i-res ==2 or (i==M and i-res >=2):
            return "YES"
    return "NO"


def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))


for i in range(int(input())):
    op(i)