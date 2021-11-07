class Solution(object):
    def countVowels(self, word):
        """
        :type word: str
        :rtype: int
        """
        vowels= {'a':0,'e':1,'i':2,'o':3 ,'u':4}
        n = len(word)
        l,r = 0,n-1
        ans =0
        acc=0
        while l <=r:
            acc += n - 2*l
            if l !=r:
                if word[l] in vowels:
                    ans += acc
                if word[r] in vowels:
                    ans += acc
            else:
                if word[l] in vowels:
                    ans += acc
            l+=1
            r-=1
        return ans 