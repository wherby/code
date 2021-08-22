from collections import defaultdict
class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) ==0:
            return True
        dict1 = [0] *1000
        for a in s:
            dict1[ord(a)] = dict1[ord(a)]+1
        res = list(filter(lambda x : x != 0,dict1))
        m = res[0]
        res = list(filter(lambda x : x != m,res))
        if len(res) ==0:
            return True
        else:
            return False
            

        

a = Solution().areOccurrencesEqual("aann")
print(a)