class Solution:
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        cnt =0
        row =[x/2 for x in row]
        n = len(row)
        for i in range(n//2):
            if row[i*2] != row[i*2+1]:
                cnt = cnt +1
                for j in range(i*2+2,n):
                    if row[i*2] == row[j]:
                        tmp = row[i*2+1]
                        row[i*2+1] = row[j]
                        row[j] = tmp
                        break

        return cnt 


s= Solution()
row=[0,2,1,3]
s.minSwapsCouples(row)