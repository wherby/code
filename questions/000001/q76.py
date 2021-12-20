from collections import defaultdict
class Solution(object):
    def minWindow(self, s, t):
        table = defaultdict(int)
        for a in t:
            table[a]+=1
        NUM = len(table.keys())
        res=""
        lens = len(s) +1
        count = 0 
        n = len(s)
        dic = defaultdict(int)
        j=0
        for i in range(n):
            dic[s[i]] +=1
            if dic[s[i]] == table[s[i]]:
                count +=1
            while count == NUM:
                if lens > i-j +1:
                    lens = i -j +1
                    res = s[j:i+1]
                dic[s[j]] -=1
                if dic[s[j]] == table[s[j]] -1:
                    count -=1
                j +=1
        return res
            