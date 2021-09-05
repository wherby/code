class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        ls= [0]*26
        for le in letters:
            t = ord(le) -ord('a')
            if ls[t] ==0:
                ls[t] =1
        ta = ord(target) - ord('a')
        for i in range(ta+1,ta+26):
            idx =  i%26
            if ls[idx] ==1:
                return chr(idx + ord('a'))
        

s=Solution()
letters = ["c", "f", "j"]
target = "g"
print s.nextGreatestLetter(letters,target)