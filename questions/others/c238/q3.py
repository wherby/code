class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """
        start =-1
        state = 0
        mx = 0
        for i,a in enumerate(word):
            if a =="a" and state !=1:
                state =1
                start =i
            if a =="e":
                if state ==1 or state ==2:
                    state =2
                else:
                    state =0
            if a =="i":
                if state ==2 or state ==3:
                    state =3
                else:
                    state =0
            if a =="o":
                if state ==3 or state ==4:
                    state =4
                else:
                    state =0
            if a =="u":
                if state ==4 or state ==5:
                    state =5
                    mx = max(mx,i-start+1)
                else:
                    state =0
        return mx
                