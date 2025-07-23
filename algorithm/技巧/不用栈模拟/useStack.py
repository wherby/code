
# https://leetcode.cn/problems/maximum-score-from-removing-substrings/description/?envType=daily-question&envId=2025-07-23
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        cnt = 0
        def getAB(s1,A,B):
            st = []
            for a in s1:
                if st and st[-1] == A and a ==B:
                    st.pop()
                else:
                    st.append(a)
            return st
        n = len(s)
        if x < y:
            s = s[::-1]
            x,y = y,x
        ls = getAB(s,"a","b")
        cnt += (n-len(ls)) //2 * x 
        n = len(ls)
        ls = getAB(ls,"b","a")
        cnt += (n-len(ls)) //2 *y 
        return cnt
