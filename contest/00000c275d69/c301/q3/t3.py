class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        ls,rs =[],[]
        tls,trs =[],[]
        n = len(start)
        a1,a2 = "",""
        for i,a in enumerate(start):
            if a =="L":
                ls.append(i)
            if a == "R":
                rs.append(i)
            if a !="_":
                a1 =a1 + a
        for i,a in enumerate(target):
            if a =="L":
                tls.append(i)
            if a == "R":
                trs.append(i)
            if a !="_":
                a2 =a2 + a
        if a1 != a2:
            return False
        for i,x in enumerate(ls):
            if ls[i]<tls[i]:
                #print("x",ls,tls)
                return False
        for i,x in enumerate(rs):
            if rs[i] > trs[i]:
               # print("y")
                return False
        return True




re =Solution().canChange(start = "R_L_", target = "__LR")
print(re)