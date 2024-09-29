# https://leetcode.cn/contest/weekly-contest-417/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/submissions/568975096/

from collections import defaultdict,deque


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowls=set(['a', 'e', 'i', 'o',  'u'])
        
        def resove(m):
            l  = 0
            c = defaultdict(int)
            ret =0
            for i,a in enumerate(word):
                if a in vowls:
                    c[a]+=1
                else:
                    c["b"]+=1
                while all(c[a] >0  for a in vowls) and c["b"]>=m:
                    if word[l] in vowls:
                        c[word[l]] -=1
                    else:
                        c["b"] -=1
                    l +=1
                ret +=l 
            return ret
                
        return resove(k) - resove(k+1)




#re =Solution().countOfSubstrings(word = "aeiou", k = 0)
re =Solution().countOfSubstrings(word = "ieaouqqieaouqq", k = 1) #3
#re =Solution().countOfSubstrings(word = "iqeaouqi", k = 2) # 2

#re =Solution().countOfSubstrings(word = "eioaua", k = 0) #2
print(re)