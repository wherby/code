class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        """
        :type differences: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        n = len(differences)
        ls =[0]*(n+1)
        for i in range(n):
            ls[i+1] = ls[i] + differences[i]
        mx = max(ls)
        mn = min(ls)
        #print(ls,mx,mn)
        if mx-mn > upper -lower:
            return 0
        else:
            return upper-lower - (mx-mn) +1

re = Solution().numberOfArrays(differences = [3,-4,5,1,-2], lower = -4, upper =3)
print(re)