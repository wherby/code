class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxN = 0
        stack =[0]
        opens =0
        for s1 in s:
            if s1 =='(':
                opens +=1
                stack.append(0)
            else:
                if opens ==0:
                    stack.append(0)
                else:
                    opens =opens -1
                    last = stack.pop() +2
                    stack[-1] = stack[-1]+ last
                    maxN= max(maxN,stack[-1])
        return maxN

# a = Solution().longestValidParentheses(")()())()()(")
# print(a)
# a = Solution().longestValidParentheses("()(()")
# print(a)
a = Solution().longestValidParentheses("()")
print(a)