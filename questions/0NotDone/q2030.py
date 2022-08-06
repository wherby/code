#https://leetcode.com/contest/weekly-contest-261/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/

class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        n = len(s)
        ls =[0]*n
        cnt =0
        for i in reversed(range(n)):
            if s[i] == letter:
                cnt +=1
            ls[i] = cnt
        st =[]
        for i,a in enumerate(s):
            while st and st[-1]>a  and len(st) + len(s)-i > k and (st[-1] != letter or repetition < ls[i]):
                if st[-1] == letter:
                    repetition +=1
                st.pop()
            if len(st) <k and (a == letter and len(st)+ repetition <= k  or len(st) + repetition <k ):
                st.append(a)
                if a == letter:
                    repetition -=1
        return "".join(st)
                        
                

re =Solution().smallestSubsequence(s = "aaabbbcccddd", k = 3, letter = "b", repetition = 2)
print(re)
        