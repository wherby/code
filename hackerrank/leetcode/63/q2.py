class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        def getDic(word):
            from collections import defaultdict
            def zero():
                return 0
            dd2 = defaultdict(zero)
            for w in word:
                dd2[w] +=1
            return dd2

        def  comp(licenseDic,dd):
            for key,value in licenseDic.items():
                if key not in dd:
                    return False
                if dd[key] < value:
                    return False
            return True
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        license = ""
        for i in licensePlate.lower():
            if i.isalpha():
                license = license + i
        licenseDic= getDic(license)
        MaxLen=100000000
        re= ""
        for word in words:
            word =word.lower()
            if len(word) > MaxLen:
                continue
            dd = getDic(word)
            if comp(licenseDic,dd):
                if len(word) < MaxLen:
                    MaxLen = len(word)
                    re = word

        return re#licenseDic

        


s= Solution()
licensePlate = "GrC8950"
words = ["measure","other","every","base","according","level","meeting","none","marriage","rest"]

print s.shortestCompletingWord(licensePlate,words)