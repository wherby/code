# https://leetcode.cn/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/solutions/3821357/an-wei-que-ding-da-an-by-tsreaper-hsai/
# 因为数字长度不长，所以可以试填最高位从小到到，看能组成的最大值满足不满足大于的要求，贪心处理
from collections import Counter
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(target)
        hf = n //2
        odv = ""
        c = Counter(s)
        left = Counter()
        for k,v in c.items():
            left[k] = v //2 
            if v%2 ==1:
                if odv != "":
                    return ""
                odv =k

        ans = []

        def dfs(idx):
            if idx == hf:
                s1 = "".join(ans)
                s1 = s1+ odv+ s1[::-1] 
                return s1  if s1 > target else ""
             
            for i in range(26):
                c1 = chr(ord('a') + i )
                if left[c1] > 0:
                    ans.append(c1)
                    left[c1] -=1 
                    tmp = "".join(ans)
                    for j in range(25,-1,-1):
                        c2 = chr(ord('a') + j )
                        if left[c2] > 0:
                            tmp +=c2*left[c2]
                    if tmp + odv + tmp[::-1] >target:
                        return dfs(idx+1) 
                    else:
                        ans.pop()
                        left[c1] +=1
            return ""
        return dfs(0)



re =Solution().lexPalindromicPermutation(s = "z", target = "z")
print(re)