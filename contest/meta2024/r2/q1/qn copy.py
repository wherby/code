

def getList(t):
    ls =[]
    for i in range(1,10-t+1):
        tmp = ""
        for j in range(t):
            tmp += str(i+j)
        ls.append(tmp)
    return ls


def resolve():
    A,B,M = list(map(lambda x: int(x),input().split()))
    cnt = 0
    T= (len(str(B))+1)//2
    for i in range(1,T+1):
        ls = getList(i)
        for a in ls:
            t = a + a[::-1][1:]
            t = int(t)
            if A<=t<=B and t %M == 0:
                cnt +=1

    return cnt

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)