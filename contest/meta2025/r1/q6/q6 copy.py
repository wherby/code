

def resolve():
    isG = False
    N, = list(map(lambda x: int(x),input().split()))
    ls =input().split()[0]
    a,b =0,0
    state = 0
    for i in range(N):
        if ls[i] == "A":
            if state <0:
                state = 0
            state +=1
        else:
            state -=1
    return "Alice" if state>0 else "Bob"

 # AAABABBBBBAAAABBAAABB   
    

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))


for i in range(int(input())):
    op(i)