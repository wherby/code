# https://leetcode.cn/problems/find-the-original-typed-string-ii/?envType=daily-question&envId=2025-07-02
# 因为数据范围是5*10**5，所有正向DP肯定会超时
# 而且K的范围是2*10**3，所有用所有情况减去不满足条件的情况就可以得到需要的答案,DP的时候仅仅需要遍历前K项
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod = 10**9+7 
        ls = []
        word = word+ "*"
        lst = ""
        state = 0
        for a in word:
            if a != lst:
                if state>0:
                    ls.append(state)
                lst =a
                state = 1 
            else:
                state+=1
        sm = 1 
        for a in ls:
            sm = sm*a %mod 
        dp = [0]* k 
        for i in range(1,min(ls[0]+1,k)):
            dp[i] =1 
        for a in ls[1:k]:
            ndp = [0]*k
            l = 0
            acc = 0  
            for i in range(1,k):
                acc += dp[i-1]
                if i-a >0:
                    acc -= dp[i-a-1]
                ndp[i] = acc%mod 
            #print(a,dp,ndp)
            dp = ndp 
        return (sm - sum(dp))%mod 