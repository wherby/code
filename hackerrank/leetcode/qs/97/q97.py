#Interleaving String
#Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

#For example,
#Given:
#s1 = "aabcc",
#s2 = "dbbca",

#When s3 = "aadbbcbcac", return true.
#When s3 = "aadbbbaccc", return false.


class Solution(object):
    #maximum recursion depth exceeded in cmp
    def isInterleaveAt(self,s1Index,S2Index,s3Index,s1,s2,s3):
        ts1 =""
        ts2 =""
        ts3 =""
        s1Valid = False
        s2Valid = False
        if s1Index< len(s1):
            ts1 =s1[s1Index]
        if S2Index< len(s2):
            ts2 = s2[S2Index]
        if s3Index< len(s3):
            ts3 = s3[s3Index]
        #print s1Index,S2Index,s3Index
        if ts1 == ts3:
            if s3Index == len(s3) -1:
                return True
            s1Valid = self.isInterleaveAt(s1Index +1 ,S2Index,s3Index+1,s1,s2,s3)
        if ts2 == ts3:
            if s3Index == len(s3) -1:
                return True
            s2Valid = self.isInterleaveAt(s1Index  ,S2Index+1,s3Index+1,s1,s2,s3)
        re= s2Valid or s1Valid
        return re

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        return self.isInterleaveAt(0,0,0,s1,s2,s3)
        
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
s4 = "aadbbbaccc"
s = Solution()
print s.isInterleave(s1,s2,s3)
print s.isInterleave(s1,s2,s4)