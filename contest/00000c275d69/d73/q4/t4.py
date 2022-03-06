# 逆序對 adjacent swap 
class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        # def removeAlready(s):
        #     n = len(s)
        #     res =""
        #     for i in range(n):
        #         if s[i] != s[n-1-i]:
        #             res += s[i]
        #     return res
        # print("befor:",s)
        # s = removeAlready(s)
        # print("after:",s)
        n = len(s)
        hf = n //2
        cnt = [0]*26
        cnt2 = [0]*26
        for a in s:
            cnt[ord(a)-ord('a')] +=1
        needM = 0
        lss = [[] for _ in range(26)]
        idx =0
        ret =""
        for i in range(n):
            t = ord(s[i]) - ord('a')
            if cnt2[t] < cnt[t] //2:
                cnt2[t] +=1
                ret += s[i]
            else:
                pass
        
            #print(k,i,n-1-k-i)
        #print(ret)
        any =""
        for i in range(26):
            if cnt[i] %2 ==1:
                any = chr(ord('a') + i)
        ret = ret + any+ ret[::-1]
        #print(ret,len(ret),len(s))
        for i in range(n):
            a = s[i]
            for j,b in enumerate(ret):
                if b ==a:
                    needM += j
                    ret = ret[:j] + ret[j+1:]
                    break
        return needM

re = Solution().minMovesToMakePalindrome("skwhhaaunskegmdtutlgtteunmuuludii")
print(re)