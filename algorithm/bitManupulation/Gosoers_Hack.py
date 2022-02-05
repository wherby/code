# Iterate all the m-bit state where there are k 1-bits.

def doSomething(state):
    print(bin(state))

def allState(k):
    m=8
    state = (1<<k) -1
    while (state <(1<<m)):
        doSomething(state)
        c = state &(-state)
        r = state +c
        state= (((r ^ state) >>2)//c) |r 
        #print("New State: ", bin(state))

allState(4)