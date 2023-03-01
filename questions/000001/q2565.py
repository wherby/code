class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        m,n = len(s),len(t)
        pre,pos = [m+1]*(n+1),[m+1]*(n+1)
        idx = 0
        ridx = m-1
        pre[0]=pos[n] = 0
        for i in range(n): 
            while idx < m:
                if s[idx] == t[i]:
                    pre[i+1] =idx +1
                    idx +=1
                    break
                idx +=1 
            while ridx >=0:
                if s[ridx] == t[n-1-i]:
                    pos[n-1-i] = m-ridx
                    ridx -=1
                    break
                ridx -=1
        mx = n
        right = 0
        for i in range(n+1):
            if pre[0] + pos[i]<=m:
                right = i 
                break
        #print(pre,pos,right)
        for i,a in enumerate(pre):
            while right < n+1 and pos[right] +pre[i] > m:
                right +=1
            if right<n+1 and pos[right] + pre[i] <= m :
                #print(mx,i,right)
                mx = min(mx,max(n- i - (n-right),0))
            if a < m:
                mx = min(mx,max(0, n-i))
        return mx



#re = Solution().minimumScore(s = "abacaba", t = "bzaa")
#re = Solution().minimumScore("cde","xyz")
re = Solution().minimumScore("adebddaccdcabaade","adbae")
print(re)