#Generate Parentheses
#
#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(p,left,right,parens=[]):
            if left: generate(p+'(',left -1 ,right)
            if right>left:generate(p+')',left,right-1)
            if not right:parens = parens.append(p)
            return parens
        return generate('',n,n)


        




s = Solution()
print s.generateParenthesis(3)