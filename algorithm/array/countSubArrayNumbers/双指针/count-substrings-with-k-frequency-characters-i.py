# 双指针 twopointers 方法复杂了 参考 slidewindow algorithm/array/countSubArrayNumbers/双指针/slidewindow.py

from collections import defaultdict,deque
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        
        n = len(s)
        cnt =0
        dic =defaultdict(int)
        lst = "-1"
        r = 0
        l=0
        while r<n:
            while dic[lst]<k and r<n:
                dic[s[r]] +=1
                lst = s[r]
                r +=1
            if dic[lst]>=k:
                while dic[lst] >=k:
                    cnt += n-r+1
                    dic[s[l]] -=1
                    l+=1
            #print(r,dic,cnt,l)
        return cnt