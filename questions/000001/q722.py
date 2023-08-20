class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        ret = []
        n = len(source)
        idx = 0 
        st = []
        findC = False
        tmp = ""
        for line in source:
            for a in line:
                if findC ==True:
                    st.append(a)
                    if len(st)>1 and st[-2:] ==['*', '/']:
                        findC = False
                        st = []
                else:
                    st.append(a)
                    if len(st)>1:
                        if st[-2:] == ['/', '/']:
                            st.pop()
                            st.pop()
                            if len(tmp+ "".join(st)):
                                ret.append(tmp+ "".join(st))
                                tmp = ""
                            st = []
                            break
                        if st[-2:] ==['/', '*']:
                            findC = True
                            st.pop()
                            st.pop()
                            tmp += "".join(st)
                            st = []
                #print(st[-2:],ret,tmp)
            if findC ==False:
                if len(st) >0:
                    tmp += "".join(st)
                    st = []
                if len(tmp)>0:
                    ret.append(tmp)
                    tmp = ""
        return ret

source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
source= ["a/*comment", "line", "more_comment*/b"]
source = ["a/*/b//*c","blank","d/*/e*//f"]
source = ["/*/bcbc//*ebdb/*/bab/*/a/*//*/d/*///*de/*///*d*//dc*///*/cd//*ccd//*a//*caacad","/*/cadaacca/*/c/*/c*//bb*////*//*e//*/*//*//*//*/ebd*//abd/*/ce*//e/*/aaa//*//*","cbae*//cc*///*/e/*//*/d*//bdeeee//*b*//de*//aceca*//dddd*///*///*deba*//abbdd/*/","dcabe/*/a/*/bdc//*cec*//ebabc//**//*//cc//*b*//*////*abdea*///*/c*//bc//*/*/ae","badcc//**//*///*/dd//*d*//*//*////*d*//eabb/*/de/*//*/*//a/*/c/*/c//*dad/*/*//"]
re = Solution().removeComments(source)
print(re)