class Solution:
    def distributeCookies(self, cookies, k: int) -> int:
        n = len(cookies)
        ls = [0]*k
        mn = sum(cookies)
        def rec(idx,ls):
            nonlocal mn
            #print(idx,ls)
            if(max(ls)> mn):
                return
            if idx ==n:
                mn = min(mn,max(ls))
                return
            for i in range(k):
                ls[i] += cookies[idx]
                rec(idx+1,ls)
                ls[i] -= cookies[idx]
        rec(0,ls)
        return mn

re =Solution().distributeCookies(cookies = [8,15,10,20,8], k = 2)
print(re)
        
        