# https://codeforces.com/blog/entry/68953

LOG_A = 30

base = [0]*LOG_A
size = 0 

def checkXor(mask):
    for i in range(LOG_A):
        if mask &(1<<i) ==0 : continue
        if base[i] == 0: return False
        mask ^= base[i]
    return True

def insertVector(mask):
    global size
    for i in range(LOG_A):
        if mask&(1<<i) == 0: continue
        if base[i] ==0:
            base[i] = mask
            size +=1
            return 
        mask ^= base[i]



insertVector(1)
print(checkXor(3))
insertVector(2)
print(checkXor(3)) 
print(checkXor(5)) 
insertVector(4)
print(checkXor(5)) 
print(checkXor(7)) 
