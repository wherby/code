# https://leetcode.cn/problems/process-string-with-special-operations-ii/?envType=daily-question&envId=2026-06-17
# 这个题目需要从后到前回溯第K位置的字符是什么的时候，在回溯的时候，需要知道k位置的字符在当前字符串的哪个位置，所以需要记录当前状态有多少个字符串，所以需要正向遍历记录当前步骤的字符串长度


class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        sz = [-1]*n 
        cur = 0
        for i,a in enumerate(s):
            if a =="*":
                cur = max(cur-1,0)
            elif a == "#":
                cur = cur*2
            elif a !="%":
                cur = cur +1
            sz[i] = cur 
        if k >= sz[-1]:
            return "."
        for i in range(n-1,-1,-1):
            a = s[i]
            csz= sz[i]
            if a =="#":
                if k >=csz//2:
                    k -= csz//2
            elif a =="%":
                k = csz -1-k 
            elif a !="*" and k == csz-1:
                return a
        

        