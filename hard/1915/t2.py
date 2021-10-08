class Solution:
    def wonderfulSubstrings(self, word) :
        count = [1] + [0]*1024
        res = cur = 0
        for c in word:
            cur ^= 1<< (ord(c)-ord('a'))
            print(cur)
            res += count[cur]  # count[cur] is the prefix of substring's status. --1
            res +=sum(count[cur ^(1<<i)] for i in  range(10))  # same idea of #1, query the prefix substring hash of number wanted.
            t =  [cur]
            for i in range(10):
                t.append(cur ^(1<<i))
            print(t)
            count[cur] +=1
            print(count[:16],res)
        return res


re = Solution().wonderfulSubstrings("ababa")
print(re)