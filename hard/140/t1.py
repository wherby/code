import functools
class Solution:
    def wordBreak(self, sr, wordDict) :
        res =[]
        n = len(sr)
        m = len(wordDict)

        @functools.lru_cache(None) 
        def dfs(lenth,arr):
            start = n-lenth
            if lenth == 0:
                res.append(arr)
            for i in range(m):
                if  len(wordDict[i]) <=lenth and wordDict[i] == sr[start: start+len(wordDict[i])]:
                    dfs(lenth - len(wordDict[i]),arr+" "+  wordDict[i])

        dfs(n,"")
        res = list(map(lambda x : x.strip(),res))
        return res

sr = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
re = Solution().wordBreak(sr,wordDict)
print(re)
            

