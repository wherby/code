class Solution(object):
    def minimumTime(self, s):
        n = len(s)
        ans = n
        ls =[0]*(n+1)
        pre = [0]*(n+1)
        for i in range(n):
            if s[i] =="1":
                ls[i]=1
            pre[i+1] = pre[i]+ls[i]
        mn =0
        for i in range(n+1):
            mn = min(mn,i - 2*pre[i])
            ans = min(ans,mn + 2*pre[i] + n-i)
        return ans
