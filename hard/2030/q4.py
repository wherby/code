class Solution(object):
    def smallestSubsequence(self, s, k, letter, repetition):
        """
        :type s: str
        :type k: int
        :type letter: str
        :type repetition: int
        :rtype: str
        """
        r2= repetition
        n = len(s)
        ls =[0]*n
        acc=0
        for i in range(n-1,-1,-1):
            if s[i] == letter:
                acc +=1
                ls[i] = acc
            else:
                ls[i] = acc
        st = []
        l = k-repetition
        #print(k,repetition,l)
        for idx,a in enumerate(s):
            #print(st,a)
            print(idx)
            while len(st) !=0 and ord(st[-1]) > ord(a) and len(st) + n-idx >k:
                if  st[-1] !=letter:
                    st.pop()
                elif ls[idx]> repetition:
                        st.pop()
                        repetition +=1 
                else:
                    break        
            st.append(a)
            if a == letter:
                repetition -=1
        res = []
        for a in st:
            if a ==letter:
                res.append(a)
            else:
                if l >0:
                    #print(l)
                    res.append(a)
                    l-=1
        print(len(res),len(st))
        return "".join(res)[:k]

s="amcdeeefghiimkklmmmnnomopqrrrssuwmyyybbbmddemmimjjmmnnpppqmtttuvvvwwmyyabccdefgiiijkklmmmopqqqmstvvwwyzacmeeeefgjkklllmmnomqrssstuvyyyzzzzbmcccceeeefgghmkkllmoopqqqsmmvwxxmymaabbbccddeeefghmjjmkmmnoopqrrsstvmwwxyyabcefggggiikllmppppqruwwwyzzzmzambbbccefgghhiijjkkkmmnnprrssuuuuwyyyzmaaabccdddefghhijjmjmjkkklorrrsssuuuwyzaamabccdddmdmemgmhmmkkmmnnoopmmsuuuvvwybcmddddmemghimjmmmmnoopmqqrstmmmwwxxyzzbdmffgmmijmmkkmmppqqrtuuvvwyyzzzzdddeeeefmfghhmiijknnpmrssssttuvxxyzbbceeemmg"
k=284
l="m"
r=64
re =Solution().smallestSubsequence(s,k,l,r)
print(re)

#abbbddeijjmabccdefgiiijkklmmmmacmeeeefgjkklllmmmbmcccceeeefgghmkkllmmmmmaabbbccddeeefghmjjmkmmmabcefggggiikllmmambbbccefgghhiijjkkkmmmaaabccdddefghhijjmjmaamabccdddmdmemgmhmmkkmmmmbcmddddmemghimjmmmmmmmmwwxxbdmffgmmijmmkkmmppqqrtuuvvwyyzzzzdddeeeefmfghhmiijknnpmrssssttuvxxyzbbceeemmg%22
#abbbddeijjmabccdefgiiijkklmmmmacmeeeefgjkklllmmmbmcccceeeefgghmkkllmmmmmaabbbccddeeefghmjjmkmmmabcefggggiikllmmambbbccefgghhiijjkkkmmmaaabccdddefghhijjmjmaamabccdddmdmemgmhmmkkmmmmbcmddddmemghimjmmmmmmmmwwxxbdmffgmmijmmkkmmppqqrtuuvvwyyzzzzdddeeeefmfghhmiijknnpmrssssttuvxxyzbbceeemmg