
def resolve():
    R,C,A,B = list(map(lambda x: int(x),input().split()))
    if R>C:
        return "YES"
    return "NO"

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)