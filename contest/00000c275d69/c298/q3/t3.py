from ctypes.wintypes import PINT

import math
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        pre= [0]*(n+1)
        ones =[]
        for i in range(n):
            if s[i] =="0":
                pre[i+1]=pre[i]+1
            else:
                ones.append(i)
        mx =0
        def dfs(ls,i, ret,acc):
            nonlocal k
            if i == len(ls):
                #print(ls,acc,ret,len(ret))
                return len(ret)
            if ls[i]=="0" and acc*2<=k:
                ret.append(ls[i])
                acc *=2
            else:
                t = (len(ls) -i-1)
                #print(t,ls,acc,i)
                if ((acc *2 +1)<<t) <=k:
                    ret.append(ls[i])
                    acc =acc*2 +1 
            return dfs(ls,i+1,ret,acc)
        mx =0
        ret = dfs(s,0,[],0)
        return ret
        
            
        
        
    
        
re =Solution().longestSubsequence(s = "00101001", k =1)
print(re)