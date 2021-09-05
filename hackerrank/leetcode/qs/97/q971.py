#Interleaving String
#Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

#For example,
#Given:
#s1 = "aabcc",
#s2 = "dbbca",

#When s3 = "aadbbcbcac", return true.
#When s3 = "aadbbbaccc", return false.


class Solution(object):

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        m =len(s1)
        n = len(s2)
        if m+ n != len(s3):
            return False
        table =[]
        for i in range(m+1):
            t1 = [0] * (n+1)
            table.append(t1)
        for i in range(m+1):
            for j in range(n+1):
                if i ==0 and j == 0:
                    table[i][j] = True
                elif i ==0:
                    table[i][j] = table[i][j-1] and s2[j-1] ==s3[i+j-1]
                elif j ==0:
                    table[i][j] = table[i-1][j] and s1[i-1] ==s3[i+j-1]
                else:
                    table[i][j] = (table[i][j-1] and s2[j-1] ==s3[i+j-1]) or (table[i-1][j] and s1[i-1] ==s3[i+j-1])
        return table[m][n]

        
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
s4 = "aadbbbaccc"
s = Solution()
print s.isInterleave(s1,s2,s3)
print s.isInterleave(s1,s2,s4)