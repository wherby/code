#https://leetcode.cn/problems/max-chunks-to-make-sorted-ii/
class Solution:
    def maxChunksToSorted(self, arr) -> int:
        stack = []
        for a in arr:
            if len(stack) == 0 or a >= stack[-1]:
                stack.append(a)
            else:
                mx = stack.pop()
                while stack and stack[-1] > a:
                    stack.pop()
                stack.append(mx)
        return len(stack)

