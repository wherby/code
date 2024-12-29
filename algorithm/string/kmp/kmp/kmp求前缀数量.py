# https://oi-wiki.org/string/kmp/#__tabbed_5_2

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


s = "abcabcabcdeabcabcabcde"
n = len(s)
pi = prefix_function(s)
print(pi)

ans = [0] * (n + 1)
for i in range(0, n):
    ans[pi[i]] += 1
#print(ans)
for i in range(n - 1, 0, -1):
    ans[pi[i - 1]] += ans[i]
for i in range(0, n + 1):
    ans[i] += 1

print(ans)