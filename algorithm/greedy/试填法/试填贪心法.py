# https://leetcode.cn/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/description/?envType=daily-question&envId=2026-08-28
# 给你两个长度均为 n 的字符串 s 和目标字符串 target，它们都由小写英文字母组成。
# 返回 字典序 最小的字符串 ，该字符串 既 是 s 的一个 回文 排列 ，又是字典序 严格 大于 target 的。如果不存在这样的排列，则返回一个空字符串。
# 如果字符串 a 和字符串 b 长度相同，在它们首次出现不同的位置上，字符串 a 处的字母在字母表中的顺序晚于字符串 b 处的对应字母，则字符串 a 在 字典序上严格大于 字符串 b。
# 排列 是指对字符串中所有字符的重新排列。

# 这个题目因为长度不是很大，所以枚举试填每一位可能的字母，然后贪心枚举试填之后最大字典序和target比较，能成功再继续，不用填的时候就考虑target  这里的复杂度应该是N*N*26 ,因为每位都要枚举26次，每次枚举的cost是N
# 因为枚举的时候从小到大，所以第一个就是符合条件最小的 
# 如果用贪心枚举的话，就从右到左贪心选取最高位都相等，然后查找比target大的是否存在 algorithm/greedy/贪心反悔法/lexPalindromicPermutation.py  这样的复杂度是 N*26

from collections import Counter
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(target)
        hf = n //2
        odv = ""
        c = Counter(s)
        left = Counter()
        mxs = []
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