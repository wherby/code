# https://leetcode.cn/problems/missing-two-lcci/
class Solution:
    def missingTwo(self, ls) :
        n = len(ls)
        ret =[]
        ls = ls +[-1]*2
        for i in range(n+2):
            while ls[i] != i+1 and ls[i] != -1:
                t = ls[i]
                ls[i],ls[t-1] = ls[t-1],ls[i]
        for i in range(n+2):
            if ls[i] == -1:
                ret.append(i+1)
        return ret

re =Solution().missingTwo([1])
print(re)