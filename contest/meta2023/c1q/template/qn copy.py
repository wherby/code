


from collections import Counter
def resolve():
    isG = True
    n,k = list(map(lambda x: int(x),input().split()))
    ls =list(map(lambda x: int(x),input().split()))
    if n>2*k:
        isG =False
    c =Counter(ls)
    for _,v in c.items():
        #print(v)
        if v>2:
            isG =False
    if isG:
        return "YES"
    else:
        return "NO"

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)