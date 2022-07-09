class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        l2 = sum(map(lambda x:len(x),words))
        m = len(words[0])
        dic = {}
        for w in words:
            dic[w] =dic.get(w,0) +1 
        ret =[]
        n = len(s)
        def dfs(idx,state,s):
            if idx == l2:
                return True
            k = s[idx : idx +m]
            if k in dic and state.get(k,0) +1 <= dic[k]:
                state[k] = state.get(k,0)+1
                if dfs(idx + m,state,s):
                    return True
            return False
        for i in range(n-l2+1):
            if dfs(0,{},s[i:i+l2]):
                ret.append(i)
        return ret

re = Solution().findSubstring(s = "barfoothefoobarman", words = ["foo","bar"])
print(re)