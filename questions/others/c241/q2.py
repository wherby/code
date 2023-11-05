class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        n1 = 0
        ls=[0]*n
        for i in range(n):
            if s[i] == "1":
                n1 +=1
                ls[i] =1
        if abs(n-2*n1) > 1:
            return -1
        def getDiff(target):
            diff = 0
            for i in range(n):
                if target[i] != ls[i]:
                    diff +=1
            return diff//2
        target = [0]*n
        if n1 > n -n1:
            for i in range(0,n,2):
                target[i] =1
            return getDiff(target)
        elif n1<n-n1:
            for i in range(1,n,2):
                target[i] =1
            return getDiff(target)
        else:
            for i in range(0,n,2):
                target[i] =1
            return min(getDiff(target),n//2-getDiff(target))


re = Solution().minSwaps("1001011")
print(re)
                     