class Solution(object):
    def maxInvestment(self, product, limit):
        """
        :type product: List[int]
        :type limit: int
        :rtype: int
        """
        product.sort(reverse=True)
        product.append(0)
        n = len(product)
        sm =0
        mod = 10**9 +7
        for i in range(1,n):
            mbt = (product[i-1]-product[i])*i
            if mbt<limit:
                limit -=mbt
                sm += i * (product[i-1] +1 + product[i]) *(product[i-1] -product[i]) //2
            else:
                l = limit//i 
                re = limit %i 
                sm += i* l * (product[i-1] + product[i-1] -l +1) //2
                sm +=  re *(product[i-1] -l) 
                return sm %mod
            #print(i,sm,product[i])
        return sm% mod

re = Solution().maxInvestment(product = [2,1,3], limit = 20)
print(re)