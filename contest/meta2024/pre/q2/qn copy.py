import math
def resolve():
    N,K = list(map(lambda x: int(x),input().split()))
    k1 = K /100
    t1 = math.log(k1)*(N-1)/N 
    a2 = math.exp(t1)
    return (a2-k1)*100


def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)