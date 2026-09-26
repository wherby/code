# https://leetcode.cn/problems/distinct-subsequences-ii/description/?envType=daily-question&envId=2026-09-07
# 给定一个字符串 s，计算 s 的 不同非空子序列 的个数。因为结果可能很大，所以返回答案需要对 10^9 + 7 取余 。
# 字符串的 子序列 是经由原字符串删除一些（也可能不删除）字符但不改变剩余字符相对位置的一个新字符串。
# 例如，"ace" 是 "abcde" 的一个子序列，但 "aec" 不是。

# 特性： 新的子序列一定 有 ls[k] 的子序列是重复的 
# total = (t1*2+1-dp[k])%mod   原有子序列 选或者不选 k 加上从空子串加上 k ,然后由于选了k的子串和 原有子串有重合，重合的数量是原有子串种k结尾的所有子串，为什么？ 因为子序列定义，原有子串k结尾的去掉k之后 一定也是独立的子串，将在这次加上k的时候重复

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod =10**9+7
        dp = [0]*26
        total = 0
        for a in s:
            k = ord(a) - ord('a')
            t1 = total
            total = (t1*2+1-dp[k])%mod 
            dp[k] = (t1+1) %mod
        return total 