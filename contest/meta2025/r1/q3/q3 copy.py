


def resolve():
    N,A,B = list(map(lambda x: int(x),input().split()))
    ret = [1]*N*2
    ret[-1] = B
    ret = [str(a) for a in ret]
    return " ".join(ret)

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+cnt)


for i in range(int(input())):
    op(i)