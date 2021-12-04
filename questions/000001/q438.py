class Solution:
    def findAnagrams(self, s: str, p: str) :
        n = len(s)
        k = len(p)
        ls =[0]*26
        for a in p:
            t = ord(a)-ord('a')
            ls[t] +=1
        ls = tuple(ls)
        lls = [0]*26
        for a in s[:k]:
            t = ord(a)-ord('a')
            lls[t] +=1
        res =[]
        for i in range(n-k+1):
            if tuple(lls) == ls:
                res.append(i)
            #print(i,lls,ls,n,k,n-k)
            if i == n-k:
                continue
            t1 = ord(s[i]) -ord('a')
            t2 = ord(s[i+k]) -ord('a')
            lls[t1] -=1
            lls[t2] +=1
        return res

re =Solution().findAnagrams("cbaebabacd","abc")
print(re)