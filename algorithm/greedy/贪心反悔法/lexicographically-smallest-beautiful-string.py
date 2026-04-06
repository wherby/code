# https://leetcode.cn/problems/lexicographically-smallest-beautiful-string/description/
# 如果一个字符串满足以下条件，则称其为 美丽字符串 ：

# 它由英语小写字母表的前 k 个字母组成。
# 它不包含任何长度为 2 或更长的回文子字符串。
# 给你一个长度为 n 的美丽字符串 s 和一个正整数 k 。

# 请你找出并返回一个长度为 n 的美丽字符串，该字符串还满足：在字典序大于 s 的所有美丽字符串中字典序最小。如果不存在这样的字符串，则返回一个空字符串。

# 对于长度相同的两个字符串 a 和 b ，如果字符串 a 在与字符串 b 不同的第一个位置上的字符字典序更大，则字符串 a 的字典序大于字符串 b 。

# 例如，"abcd" 的字典序比 "abcc" 更大，因为在不同的第一个位置（第四个字符）上 d 的字典序大于 c 。s

# 回文子字符串的性质: 如果一个字符串不存在长度为2,3 的回文字符串，则该字符串不是回文字符串
# 此题目采用贪心进位的操作
class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        sc= ord('a') + k
        ls = [ord(a) for a in s]
        n = len(s)
        idx = 0
        ls[n-1] +=1
        while 0<= idx< n:
            if ls[idx] == sc and idx ==0: #失败条件
                return ""
            elif ls[idx] == sc:  #反悔前一位
                ls[idx] =ord("a")
                idx -=1
                ls[idx] +=1
            elif (idx and ls[idx-1] == ls[idx] or( idx >1 and ls[idx-2]==ls[idx]) ):
                ls[idx]+=1
            else:
                idx +=1
        return "".join([chr(a) for a in ls])