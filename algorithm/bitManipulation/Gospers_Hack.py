# Iterate all the m-bit state where there are k 1-bits.
cnt =0
res = []
def doSomething(state):
    global cnt
    print(bin(state))
    res.append('{:08b}'.format(state))
    cnt +=1
    print(cnt)

def allState(k,m=8):
    state = (1<<k) -1
    while (state <(1<<m)):
        doSomething(state)
        c = state &(-state)
        r = state +c
        state= (((r ^ state) >>2)//c) |r 
        #print("New State: ", bin(state),state <(1<<m),state,1<<m)

allState(2)
print(res)