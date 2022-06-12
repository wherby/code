from collections import defaultdict
class Solution(object):
    def matchReplacement(self, s, sub, mappings):
        """
        :type s: str
        :type sub: str
        :type mappings: List[List[str]]
        :rtype: bool
        """
        m,n = len(s),len(sub)
        dic =defaultdict(set)
        for a,b in mappings:
            dic[a].add(b)
        def compare(left,right):
            for i in range(n):
                if left[i] != right[i] and left[i] not in dic[right[i]]:
                    return False
            return True
        for i in range(m-n+1):
            if compare(s[i:i+n],sub):
                return True
        return False

re = Solution().matchReplacement(s = "fool3e7bar", sub = "leet", mappings = [["e","3"],["t","7"],["t","8"]])
print(re)
        