
from collections import defaultdict,deque


def resolve():
    m = int(input())
    ols = input()
    arr =[0]*(m+1)
    for i,a in enumerate(ols,1):
        if a == "1":
            arr[i]=1
    n = int(input())
    c = defaultdict(int)
    for _ in range(n):
        a = int(input())
        c[a] +=1
    cnt = 0
    dic=defaultdict(int)
    for i in range(1,m+1):
        if arr[i] ==1:
            cnt +=1
            dic[i] =1
            for j in range(i,m+1,i):
                arr[j] = 1- arr[j]
    for k,v in c.items():
        if v %2 ==1:
            dic[k] +=1
            if dic[k] %2 ==0:
                cnt -=1
            else:
                cnt +=1
    return cnt

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)