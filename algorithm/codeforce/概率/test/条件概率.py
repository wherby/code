    # https://codeforces.com/gym/105478/problem/B
# Not work
from functools import cache

def testString(s1):
    n= len(s1)
    acc =0 
    ss= ["A","B","C"]
    ans = 0

    dp = [1]*n

    @cache
    def dfs(idx,last):
        nonlocal ans
        if idx == n:
            return 1 
        if last == s1[idx]:
            return 0
        re =[]
        if s1[idx] =="?":
            for st in ss:
                if st !=last:
                    k1 =  dfs(idx+1,st)
                    if k1 != 0:
                        re.append(k1)
            if len(re) ==0:
                return 0
            dp[idx] = min(min(re)/sum(re),dp[idx])
            return max(re)
        else:
            dp[idx] =1 
            return dfs(idx+1,s1[idx])
    dfs(0,-1)
    for i in range(n):
        ans += dp[i]
    print(dp)
    return ans
            




t1 = "A??B?C"
t1 = "A???A"
print(testString(t1))