# https://leetcode.com/contest/weekly-contest-261/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/
class Solution(object):
    def smallestSubsequence(self, s, k, letter, repetition):
        """
        :type s: str
        :type k: int
        :type letter: str
        :type repetition: int
        :rtype: str
        """
        st =[]
        sm =0 
        for a in s:
            if a == letter:
                sm +=1
        rm = sm- repetition
        #print(sm,rm)
        n = len(s)
        mlen =k-repetition
        rmo = n-k
        for i,a in enumerate(s):
            while st and (ord(a)<ord(st[-1]) and ((st[-1] == letter and rm >0) or (st[-1] != letter and rmo >0 ))):
                b=st.pop()
                rmo -=1
                if b==letter:
                    mlen -=1
                    rm -=1
            if len(st)== mlen and a != letter:
                continue
            st.append(a)
            if a ==letter:
                mlen +=1
        #print(st,rm)
        return "".join(st[:k])

re = Solution().smallestSubsequence( "mmmxmxymmm",8,"m",4)
print(re)