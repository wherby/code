# https://leetcode.cn/problems/find-the-string-with-lcp/description/?envType=daily-question&envId=2026-03-28
# 因为需要找到字典序最小的字符串，所以贪心试填每一位，因为会遍历每个位置，所以只需判断lcp[i][j]>0 即可
# 在验证阶段再判断lcp[i][j]的值是否正确



from typing import List, Tuple, Optional

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n =len(lcp)
        cur = "a"
        ret = [""]*n 
        for i in range(n):
            if ret[i] =="":
                ret[i] = cur 
                cur = chr(ord(cur)+1)
                if ord(cur)>ord('z')+1:
                    return ""
            for j in range(i,n):
                if lcp[i][j]>0:
                    if ret[j] =="":
                        ret[j] = ret[i]
                    elif ret[j] != ret[i]:
                        return ""
        for i in range(n):
            for j in range(n):
                if ret[i] == ret[j]:
                    if i+1<n and j +1<n :
                        if lcp[i][j] != lcp[i+1][j+1]+1:
                            return ""
                    else:
                        if lcp[i][j] !=1:
                            return ""
                elif lcp[i][j] != 0:
                    return ""
        return "".join(ret)
                    
