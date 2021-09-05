class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        ls = [i for i in range(L,R+1)]
        pl = [2,3,5,7,11,13,17,19,23,29] 
        dpl = {}
        for i in pl:
            dpl[i] =1
        bls = map(lambda x: "{0:b}".format(x),ls)
        def cntOne(x):
            cnt =0
            for  i in x:
                if i == "1":
                    cnt = cnt +1
            if cnt in dpl:
                return 1
            else:
                return 0

        cntbls = map(cntOne, bls)
        return sum(cntbls)



s= Solution()
print s.countPrimeSetBits(6,10)