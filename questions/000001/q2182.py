class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        ls = [0]*26
        dic ={}
        rdic={}
        for i,a in enumerate('abcdefghijklmnopqrstuvwxyz'):
            dic[a] = i
            rdic[i] =a
        for a in s :
            ls[ord(a) - ord('a')] +=1
        res = []
        idx = 25
        while idx >= 0:
            if ls[idx] > repeatLimit:
                res.append(rdic[idx]*repeatLimit)
                ls[idx] -= repeatLimit
                isFind = False 
                for j in range(idx-1,-1,-1):
                    if ls[j] >0:
                        ls[j] -=1
                        isFind = True
                        res.append(rdic[j])
                        break
                if not isFind:
                    break
            else:
                res.append(rdic[idx]*ls[idx])
                ls[idx] = 0
                idx -=1
        #print(res)
        return "".join(res)
                
                
re = Solution().repeatLimitedString(s = "aababab", repeatLimit = 2)
print(re)