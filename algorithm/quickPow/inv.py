# inv  逆元
# https://github.com/wisdompeak/LeetCode/tree/master/Template/Inverse_Element


# method1
mod = 10**9 +7
def quickPow(x,y):
    ret =1
    cur = x 
    while y >0:
        if y & 1:
            ret = ret * cur % mod
        cur = cur *cur % mod
        y = y //2
    return ret

def inv(x):
    return quickPow(x,mod-2)


# method2
mod = 10**9 +7
def inv2(x):
    s= 1
    while x >1:
        s= s*(mod-mod//x)%mod
        x = mod%x
    return s

print(inv(100),inv2(100))