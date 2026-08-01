
from collections import Counter
import math
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        m = n //2 
        c = Counter(s[:m])
        cnt=[0]*26
        for k1,v in c.items():
            cnt[ord(k1) -ord('a')] = v 
        
        def perm(m):
            acc =0 
            cur = 1 
            for a in cnt:
                if a ==0:
                    continue
                cur = cur * math.comb(acc+a,a)
                acc +=a 
                if cur >=k:
                    return k 
            return cur 
        #print(cnt,perm(m))
        if perm(m) < k:
            return ""
        
        ret = [""]*m 
        for i in range(m):
            for j in range(26):
                if cnt[j] ==0:continue
                cnt[j] -=1
                if perm(m-i-1) >=k:
                    ret[i] = chr(ord('a') +j)
                    break
                k -= perm(m-i-1)
                cnt[j] +=1
        if n%2 ==1:
            ret.append(s[m])
        ret.extend(ret[:m][::-1])
        return "".join(ret)

ret = Solution().smallestPalindrome( s = "abba", k = 2)
print(ret)