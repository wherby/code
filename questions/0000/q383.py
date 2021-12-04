class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for a in magazine:
            dic[a] +=1
        for r in ransomNote:
            t = dic.get(r,0)
            if t == 0:
                return False
            dic[r] = t-1