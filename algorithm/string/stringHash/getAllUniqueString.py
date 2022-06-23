# https://wherby.github.io/code/string/string-hashing.html

## Get all unique substring of string input

def countUniqueSubString(str1):
    n = len(str1)
    p  =31
    m  = 10**9+9
    p_pow = [0]*n
    p_pow[0] =1
    for i in range(1,n):
        p_pow[i] = p_pow[i-1]*p %m
    
    h = [0]*(n+1)
    for i in range(n):
        h[i+1] = (h[i] + (ord(str1[i])-ord('a')+1)*p_pow[i])%m
    
    cnt = 0
    for l in range(1,n+1):
        hs =set()
        for i in range(n-l+1):
            cur_h = (h[i+l] +m - h[i]) %m 
            cur_h = (cur_h * p_pow[n-i-1])%m 
            hs.add(cur_h)
        cnt += len(hs)
    return cnt

str1 ="a"*1000
print(countUniqueSubString(str1))
str1 = "abcdefab"
print(countUniqueSubString(str1))