class Solution(object):
    def smallestSubsequence(self, s, k, letter, repetition):
        n = len(s)
        delete = n-k
        stack =[]
        pre =0
        remain = s.count(letter)
        for i in range(n):
            while delete and stack and stack[-1] > s[i]:
                if stack[-1] == letter:
                    if pre -1 + remain < repetition:
                        break
                    pre -=1
                stack.pop()
                delete -=1
            if s[i] == letter:
                pre +=1
                remain -=1
            stack.append(s[i])
        while len(stack) > k:
            if stack.pop() ==letter:
                pre -=1
        for i in range(k-1,-1,-1):
            if pre <repetition and stack[i] != letter:
                stack[i] = letter
                pre +=1
            if pre == repetition:
                break
        return "".join(stack)