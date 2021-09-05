class WordFilter(object):
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.ls=[]
        self.rls=[]
        cnt =0
        self.dic={}
        for word in words:
            #print word
            rword = word[::-1]
            self.ls.append(word)
            self.rls.append(rword)
            self.dic[word] =cnt
            cnt = cnt +1

        self.ls= sorted(self.ls)
        self.rls = sorted(self.rls)
        #print self.ls,self.rls
        

    def f(self, prefix, suffix):
        import bisect
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        if len(self.ls)==0:
            return -1 
        #print prefix, " : " ,suffix
        suffix = suffix[::-1]
        suffix2 =suffix
        prefix2 = prefix
        prefixStart = 0
        prefixEnd = len(self.ls)
        suffixStart =0
        suffixEnd =len(self.ls)
        if len(prefix) >0:
            prefixStart = bisect.bisect_left(self.ls,prefix)
            prefix2 = prefix[:len(prefix)-1] + str(chr(ord(prefix[-1])+1))
            prefixEnd = bisect.bisect_right(self.ls,prefix2)
        if len(suffix2) >0:
            suffixStart = bisect.bisect_left(self.rls,suffix)
            suffix2 = suffix[:len(suffix)-1] + str(chr(ord(suffix2[-1])+1))
            suffixEnd = bisect.bisect_right(self.rls,suffix2)
        prels= self.ls[prefixStart: prefixEnd]
        sufls = self.rls[suffixStart:suffixEnd]
        dic1 ={}
        for t1 in prels:
            dic1[t1] =1
        num =-1
        for t2 in sufls:
            t2 = t2[::-1]
            if t2 in dic1:
                if self.dic[t2] >num:
                    num = self.dic[t2] 
        return num

        
        


w = WordFilter(["pop","cas","zca","dre"])
print w.f("a", "e")
print w.f("", "op")