class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        n = len(s)
        ls =[]
        for x in s:
            ls.append(int(x))
        res = []
        def add(a,ls):
            for i in range(1,n,2):
                ls[i] = (ls[i] + a) %10
            res.append(tuple(ls))
            return ls
        def shift(b,ls):
            ls = ls[n-b:]+ ls[:n-b]
            res.append(tuple(ls))
            return ls
        lss =[]
        for i in range(20):
            ls =  shift(b,ls)
            #ls = min(ls,ls2)
            for j in range(11):
                ls = add(a,ls)
                for _ in range(n):
                    ls =  shift(b,ls)
        # print(ls)
        # ls =shift(b,ls)
        # ls =add(a,ls)
        # ls =shift(b,ls)
        # print(ls)
        #print(res)
        res = sorted(res)
        
        re1= "".join(map(lambda x:str(x), res[0]))
        #print(re1)
        return re1

re= Solution().findLexSmallestString(s = "5562438547", a = 1, b = 3)
print(re)
        