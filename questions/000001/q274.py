class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        n = len(citations)
        for i in range(n):
            a = citations[i]
            le = n - i
            if a>=le:
                return le
        return 0

re = Solution().hIndex(citations = [0])
print(re)