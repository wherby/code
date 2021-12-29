class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <2:
            return ""
        n = len(palindrome)
        for i in range(n):
            if palindrome[i] !="a":
                t = palindrome[:i] + "a" +palindrome[i+1:]
                if t!= t[::-1]:
                    return t
        for i in range(n-1,-1,-1):
            if palindrome[i] =="a":
                t = palindrome[:i] + "b" +palindrome[i+1:]
                if t!= t[::-1]:
                    return t  
re =Solution().breakPalindrome("abccba")  
print(re)