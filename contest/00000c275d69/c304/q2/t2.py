class Solution(object):
    def maximumGroups(self, grades):
        """
        :type grades: List[int]
        :rtype: int
        """
        n = len(grades)
        if n ==1:
            return 1
        for i in range(1,n+1):
            if i*(i+1)/2 >n:
                break
        return i-1





re =Solution().maximumGroups([1])
print(re)