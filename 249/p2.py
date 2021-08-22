class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr=[]
        n = len(s)
        for i in range(0,1000):
            arr.append([10000000,0])
        for j in range(0,n):
            i = ord(s[j]) 
            if j < arr[i][0]:
                arr[i][0] = j
            if j > arr[i][1]:
                arr[i][1] = j 
        cnt = 0
        for p1 in arr:
            dic1 ={}
            if p1[0]< p1[1]:
                for i in range(p1[0]+1, p1[1]):
                    k = ord(s[i]) 
                    if k not in dic1:
                        cnt = cnt +1
                        dic1[k] =1
        return cnt
s1 = "a11a"
a=Solution().countPalindromicSubsequence(s1)
print(a)