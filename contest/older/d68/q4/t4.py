class Solution(object):
    def abbreviateProduct(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: str
        """
        sm = 1
        zer =0
        bigSm =0
        for i in range(left,right+1):
            sm = sm*i
            if bigSm>0:
                bigSm = bigSm*i
            while sm%10 ==0:
                sm = sm //10
                zer +=1
            if bigSm > 10**100:
                bigSm = bigSm//(10**90)
            if sm >(10**100):
                sm1= sm
                sm = sm %(10 **90)
                if bigSm ==0:
                    bigSm = sm1 //(10**90)
        if bigSm ==0:
            if sm > 10**10:
                little = sm %(10**5)
                bigend = sm
                while bigend > (10**5):
                    bigend = bigend //10
                return str(bigend) + "..." +"{:05}".format(little) + "e" + str(zer)
            else:
                return str(sm) + "e" + str(zer)
        else:
            little  = sm %(10**5)
            bigend = bigSm
            while bigend > (10**5):
                bigend = bigend//10
            return str(bigend) + "..." + "{:05}".format(little) + "e" + str(zer)

            
# re = Solution().abbreviateProduct(256,65535)
# print(re)
# #@print(sm)
# re = Solution().abbreviateProduct(left = 999998, right = 1000000)
# print(re)
# re = Solution().abbreviateProduct(left = 2, right = 11)
# print(re)
re = Solution().abbreviateProduct(left = 8, right = 18)
print(re)