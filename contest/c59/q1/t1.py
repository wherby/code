class Solution:
    def minTimeToType(self, word):
        if len(word) ==0:
            return 0
        word ="a"+word
        ordlist = list(map(lambda x: ord(x),word))
        cnt = 0
        for i in range(1,len(ordlist)):
            t = (ordlist[i] -ordlist[i-1] +26 )%26
            if t < 13:
                cnt = cnt +1 + t 
            else:
                cnt = cnt +26 -t +1
        return cnt



a= Solution().minTimeToType("bza")
print(a)