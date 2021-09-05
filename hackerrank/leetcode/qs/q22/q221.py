#Generate Parentheses
#
#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



class Solution(object):
    def __init__(self):
        self.parens =[]
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(p,left,right):
            if left: generate(p+'(',left -1 ,right)
            if right>left:generate(p+')',left,right-1)
            if not right:self.parens.append(p)
        generate('',n,n)
        return self.parens


        




s = Solution()
print s.generateParenthesis(3)