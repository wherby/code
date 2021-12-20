from collections import defaultdict
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        dic = defaultdict(int)
        for a in allowed:
            dic[a] =1
        cnt =0
        for word in words:
            isMa = True
            for w in word:
                if w not in dic:
                    isMa =False
                    break
            if isMa:
                cnt+=1
        return cnt
            