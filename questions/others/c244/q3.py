class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(map(lambda x:int(x),s))
        n = len(s)
        left0l = [0]*n
        left10 = [0]*n
        right01 =[0]*n
        right10 =[0]*n
        def compare(start,ls,s):
            cnt =0
            for i in range(n):
                if start ^1 !=s[i]:
                    cnt +=1
                start = start ^1
                ls[i] =cnt
        revS = s[::-1]
        compare(1,left0l,s)
        compare(0,left10,s)
        compare(1,right01,revS)
        compare(0,right10,revS)
        #print(left0l)
        mn = min(left0l[-1],left10[-1],right01[-1],right10[-1])
        for i in range(n-1):
            t = left0l[i] + right10[n-i-2]
            t2 = left10[i] + right01[n-i-2]
            mn = min(mn,t,t2)
        return mn

re = Solution().minFlips("100101011101000001010010110")
print(re)