# Get sub state 


state =254

def getSubState(state):
    ret = []
    j = state&(state -1)
    while j :
        ret.append(j)
        j = (j-1)&state 
    return ret 

ret = getSubState(state)
print([bin(a)[2:] for a in ret])
print(len(set(ret)))