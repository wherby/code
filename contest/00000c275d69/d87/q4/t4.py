class Solution(object):
    def minimumMoney(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        mx =0
        acc =0
        mmx = 0
        for a,b in transactions:
            if a >b:
                acc += a-b
                mmx =max(mmx,b)
            else:
                mx = max(mx,a)
        return acc +max(mmx,mx)
                




re =Solution().minimumMoney(transactions = [[3,0],[0,3]])
print(re)