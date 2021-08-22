from collections import defaultdict
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        n = len(words)
        k = len(words[0])
        if len(s )< n*k:
            return []
        res = []
        mask = [0]*n
        dic =defaultdict(int)
        for i in range(n):
            dic[words[i]] = dic[words[i]]+1

        m = len(s)
        for i in range(0,m-n*k+1):
            dic2 =dic.copy()
            st = s[i:i+n*k]
            #print(st)
            for j in range(n):
                stt = st[j*k:(j+1)*k]
                #print(stt)
                if stt not in dic:
                    break
                else:
                    dic2[stt]= dic2[stt] -1
            isSet = len(list(filter(lambda x : x !=0 ,dic2.values()))) ==0
            #print(mask, isSet)
            #print(list(dic2.values()))
            if isSet:
                res.append(i)
        return res

a = Solution().findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"])
print(a)

