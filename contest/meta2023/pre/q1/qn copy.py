def resolve():
    isG = True
    a,b,c = list(map(lambda x: int(x),input().split()))
    if a + 2*b <c:
        isG =False
    if 2*a + 2*b < c+1:
        isG =False
    #print(a,b,c)
    if isG:
        return "YES"
    else:
        return "NO"

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)