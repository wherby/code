
class Solution:
    def dfs(self, s,words,mask,index):
        if index == len(s):
            self.find = True
            return
        if self.find == True:
            return
        for i in range(len(words)):
            if 1<<i & mask ==0:
                t1 = len(words[i])
                if s[index:index +t1] == words[i]:
                    self.dfs(s,words,mask| 1<<i, index+t1)
    def isPrefixString(self, s, words):
        n = len(s)
        cnt = 0
        t = 0
        index =0
        while t <n and index<len(words):
            t += len(words[index])
            index = index +1
            cnt = cnt+1
        if t != n:
            return False
        index =0
        for i in range(cnt):
            if words[i] != s[index :index +len(words[i])]:
                return False
            index = index +len(words[i])
        return True





s = "iloveleetcode"
words = ["i","love","leetcode","apples"]
print(Solution().isPrefixString(s,words))
print(Solution().isPrefixString("ccccccccc",["c","cc"]))
print(Solution().isPrefixString("applebananacookie",["banana","apple","cookie"]))