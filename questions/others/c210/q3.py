class Solution(object):
    def checkPalindromeFormation(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """
        n =len(a)
        m = len(b)
        if n <=1:
            return True
        t1 =a+b
        t2 =b+a
        def manachers(S):
            A = "@#" + "#".join(S) + "#$"
            Z = [0] * len(A)
            center = right =0
            for i in range(1,len(A)-1):
                if i < right:
                    Z[i] = min(right -i,Z[2*center -i])
                while A[i + Z[i]+1] == A[i-Z[i]-1]:
                    Z[i] +=1
                if i + Z[i] > right:
                    center,right = i , i+ Z[i]
            return Z[2:-2:1]
        


        re= manachers(a)
        #print(re)
        re2 = manachers(b)
        #print(re2)
        i =0
        while a[i] == b[n-1-i]:
            i+=1
        if i-1 < n//2:
            #print(i)
            #print(re2[m-1],re[n-1],m-i*2,n-i*2)
            if re[n-1] >= n-i*2:
                return True
            if re2[m-1] >= m -i*2:
                return True
        else:
            return True
        i=0
        while b[i] == a[n-1-i]:
            i+=1
        if i-1 < n//2:
            #print(i)
            #print("cc")
            #print(re2[n])
            if re[n-1] >= n-i*2:
                return True
            if re2[m-1] >= m -i*2:
                return True
        else:
            return True
        return False

a = "nujdzwsoxzqfuglhqsrdhkejqdmwmemcosketqvoofnkhovzmzwxmurqbjqcjzpiszfctddbaqggudbcsnqjcuhdicrzsdnxkfubuzwpfrldnavdbovdfcgftuynfddntwrujcnlamzikredxouyurorftftgzdikwrejuxodyssqokbsonwjnqskxrsjphhqlcjlruaymbvmjuqoipcvzhysjbctbkwnjahnbofsbgniwbathobuviagztjpgrexfzgfoizudnrvxnfdrpprawydgiwzfjunmfrnuwbctqqcdxvqroqdicooswbqhzgakniguosawotuhimqovnzlfcvubmkfvndjeigpemyflsqngtetrpcoqnbelcsykmcgroxgnuxfdtrqdftjenghvytbupwyvuhpjxnonurwfsnihjjzgmscgirnwwbtbpoczktrflwxsjkuhaoawzsreqouuhgluuthbzwqexqaurfscetmymtrqivlxbjuejkxfcysahxgitbmiqitvhetbiptbkoviicvunlecbnhoosgsartkobzqchwsltvefijezsggucnvreb"
b="svxoxobteochtybipwvgwpduyuvgcrsjvnwuktzvgnrlkzcooixejqfkwdqhzectytqngsdwxorhvffelcumnddxfaogjnemgmohycxmevukxcnukeengmhgnnfgwyreiedpsiojjqqzdthwsdnwyclowmslxehbgyfjqwprqeztpaaqdnvubknjwvzufzejncaouzentnbzxgdjlunqllymbhmxjwuznzmlnoqwmwwrdhqdqoqtzrjsoepgzktqcmprpsqjxlpwehtrcmqudqwucahmdljdwerydznnzdyrewdjldmhacuwqduqmcrthewplxjqsprpmcqtkzgpeosjrztqoqdqhdrwwmwqonlmznzuwjxmhbmyllqnuljdgxzbntnezuoacnjezfuzvwjnkbuvndqaaptzeqrpwqjfygbhexlsmwolcywndswhtdzqqjjoispdeierywgfnnghmgneekuncxkuvemxcyhomgmenjgoafxddnmucleffvhroxwddtcfzsipzjcqjbqrumxwzmzvohknfoovqteksocmemwmdqjekhdrsqhlgufqzxoswzdjun"
re = Solution().checkPalindromeFormation(a,b)
print(re)