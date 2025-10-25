

from itertools import pairwise
def resolve():
    ret = 0
    N = list(map(lambda x: int(x),input().split()))
    ls =list(map(lambda x: int(x),input().split()))
    for a,b in pairwise(ls):
        ret = max(ret,abs(a-b))
    return ret

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))


for i in range(int(input())):
    op(i)