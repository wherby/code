# https://cp-algorithms.com/string/prefix-function.html
def prefix_function(s):
    n = len(s)
    pi = [0]*n
    for i in range(1,n):
        j = pi[i-1]
        while j >0 and s[i] != s[j]:
            j  = pi[j-1]
        if s[i] == s[j]:
            j +=1
        pi[i] = j 
    return pi

pat = "ABABCABAB"
next = prefix_function(pat)
print(next)

# count the prefix s[:i] appears in s 
#
# pi: the next array in KMP
def countPrefix(pi):
    n =len(pi)
    ans = [0]*(n+1)
    for i in range(n):
        ans[pi[i]] +=1
    for i in range(n-1,0,-1):
        ans[pi[i-1]] += ans[i] 
    for i in range(1,n+1):
        ans[i] +=1
    return ans

re = countPrefix(next)
print(re)
# [9, 4, 4, 2, 2, 1, 1, 1, 1, 1]  which means "" shows 9 times in the s ,"a" shows 4 times , "ab" shows 4 times in "ABABCABAB"


# compress the string, find the stortest component to compress origin string 
#
#
a = "abcabcabcabc"
next = prefix_function(a)
print(next)
n = len(a)
for i in range(n-1,-1,-1):
    t = next[i]
    if  n%(n-t) ==0:
        print(n- t)
        break