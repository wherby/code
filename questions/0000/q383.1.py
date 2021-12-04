from collections import Counter 
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = Counter(ransomNote) 
        b = Counter(magazine)
        print("a=",a," b =",b, " a&b=",a&b)
        return (a & b) == a

re = Solution().canConstruct("aaaaa","aaab")
re = Solution().canConstruct("aa","aaab")