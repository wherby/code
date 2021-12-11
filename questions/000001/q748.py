from collections import defaultdict
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        def getDic(word):
            dic =defaultdict(int)
            for a in word:
                if a.isalpha():
                    dic[a.lower()] +=1
            return dic

        aDic = getDic(licensePlate)
        def comparev(dic1,dic2):
            for k,v in dic1.items():
                if k not in dic2:
                    return False
                if v > dic2[k]:
                    return False
            return True
        res = []
        lena = 10**10
        for word in words:
            dic2 = getDic(word)
            if comparev(aDic,dic2):
                if len(word) < lena:
                    lena = len(word)
                    res = [word]
                if len(word) == lena:
                    res.append(word)
        #print(res)
        return res[0]

re = Solution().shortestCompletingWord(licensePlate = "B687015", words =["born","give","would","nice","in","understand","blue","force","have","that"])
print(re)


        