class Solution(object):
    def countVowels(self, word):
        """
        :type word: str
        :rtype: int
        """
        vowels= {'a':0,'e':1,'i':2,'o':3 ,'u':4}
        n = len(word)
    
        res = 0
        for i in range(n):
            if word[i] in vowels:
                res += (i+1) * (n-i)
        return res



def test(str):
    vowels= {'a':0,'e':1,'i':2,'o':3 ,'u':4}
    n = len(str)
    cnt = 0
    for i in range(n):
        for j in range(i+1,n+1):
            sb = str[i:j]
            #print(sb)
            for a in sb:
                if a in vowels:
                    cnt +=1
    print(cnt)

str =["pppppppppp",
      "appppppppp",
      "aapppppppp",
      "aaappppppp",
      "aaaapppppp",
      "aaaaappppp",]
n =len(str)
for i in str:
    test(i)

re=Solution().countVowels(word = "noosabasboosa")
print(re)
#aaa => 4 =>10 
#ab => 2
#bba =>3
#bab=>4
#baba=>ba a bab ab / a ba aba baba
#ba => 2 
#bab => 4
#baba => a ba aba baba
# 1,4,10
#02 7 16