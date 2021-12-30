class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        dic1,dic2,dic3= {},{},{}
        vowels = ["a","e","i","o","u"]
        for w in wordlist:
            dic1[w] = w
            if w.lower() not in dic2:
                dic2[w.lower()]=w
            ls = ""
            for a in w:
                if a.lower() not in vowels:
                    ls +=a.lower()
                else:
                    ls += "*"
            if ls not in dic3:
                dic3[ls] = w
        res =[]
        for q in queries:
            ls = ""
            for a in q:
                if a.lower() not in vowels:
                    ls +=a.lower()
                else:
                    ls += "*"
            #print(ls,dic3)
            if q in dic1:
                res.append(dic1[q])
            elif q.lower() in dic2:
                res.append(dic2[q.lower()])
            elif ls in dic3:
                res.append(dic3[ls])
            else:
                res.append("")
        return res

#re = Solution().spellchecker(wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"])
#re = Solution().spellchecker(["YellOw"],["yollow"])
re = Solution().spellchecker(["ae","aa"],["UU"])
print(re)
        