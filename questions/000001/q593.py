import itertools
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        ls = [p1,p2,p3,p4]
        fd = False
        def dis(p1,p2):
            return (p1[0]-p2[0])**2 + (p1[1] -p2[1])**2
        for comb in itertools.permutations(ls):
            p1,p2,p3,p4 = comb
            if dis(p1,p2) == dis(p2,p3) ==dis(p3,p4) == dis(p4,p1) and dis(p1,p3) ==dis(p2,p4):
                fd = True
        return fd
            

re = Solution().validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1])
print(re)
        