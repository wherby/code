class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        m = len(rolls)
        sm = mean *(m+n) - sum(rolls)
        if sm >n*6 or sm <n:
            return []
        res =[1] * n
        sm = sm -n
        for i in range(n):
            if sm ==0:
                continue
            if sm >=5:
                res[i] =6
                sm -=5
            else:
                res[i] = sm +1
                sm =0
        return res