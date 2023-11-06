from itertools import combinations,permutations
class Solution(object):
    def nextBeautifulNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr= []
        for i in range(7):
            arr.append([i+1]*(i+1))
        m = len(str(n))
        def dp(msk):
            res =[]
            cnt =0
            while msk >0:
                t1 = msk %2
                if t1 ==1:
                    res = res + arr[cnt]
                msk =msk //2
                cnt +=1
            if len(res) > m+1:
                return 1000000000000000000
            cand = list(permutations(res))
            mx =1000000000000000000
            for c1 in cand:
                num= 0
                for c2 in c1:
                    num = num *10 + c2
                if num > n :
                    mx = min(mx,num)
            return mx
        mx =100000000000000000
        for i in range(8):
            r = dp(i)
            print(r,i)
            mx =min(mx,r)
        return mx

re =Solution().nextBeautifulNumber(1000)
print(re)        