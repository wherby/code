# https://cp-algorithms.com/string/rabin-karp.html
# Not verifyied by test


def rabin_karp(s,t):
    p = 31
    m = 10**9+9
    sl,tl = len(s),len(t)
    p_pow = [1] * max(sl,tl)
    for i in range(1,max(sl,tl)):
        p_pow[i] = (p_pow[i-1]*p) %m
    
    tls = [0] *(tl+1)
    for i in range(tl):
        tls[i+1]  =(tls[i] +(ord(t[i]) -ord('a') +1)*p_pow[i]) %m
    
    h_s =0
    for i in range(sl):
        h_s= (h_s + (ord(s[i]) - ord('a') +1)*p_pow[i]) %m 
    
    res =[]
    for i in range(0,tl-sl +1):
        h_cur = (tls[i+sl] + m - tls[i])%m
        if h_cur  == h_s * p_pow[i] %m :
            res.append(i)
    return res

s = "abd"
t = "abdndnabdmabd"
re = rabin_karp(s,t)
print(re)