from typing import List, Tuple, Optional
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        dic = {}
        res = []
        for a in names:
            if a not in dic:
                b = a.split()
                dic[a] =0
                res.append(a)
            else:
                b = dic[a]
                b +=1
                for i in range(b, 10**5):
                    c= a +"(" + str(i) + ")"
                    if c not in dic:
                        res.append(c)
                        dic[c] =0
                        dic[a] = i
                        break
        return res

re = Solution().getFolderNames(["kaido","kaido(1)","kaido","kaido(1)"])
print(re)