from functools import cache
class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        @cache
        def search(idx):
            ret =1
            for i in range(1,(n-idx)//2 +1):
                if s[idx:i+idx] == s[idx+i:idx+i*2]:
                    ret = max(ret , search(idx +i) +1)
            return ret
        return search(0)