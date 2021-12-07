from collections import defaultdict
class Solution:
    def minDeletions(self, s: str) -> int:
        dic = defaultdict(int)
        for a in s:
            dic[a]+=1
        ls = list(dic.values())
        ls.sort()
        cnt = 0
        last = 1000000000
        for i in ls[::-1]:
            #print(i,last)
            if i < last:
                last =i
            else:
                cnt += min(i-last+1,i)
                last = last -1
        return cnt

re = Solution().minDeletions("bbcebab")
print(re)