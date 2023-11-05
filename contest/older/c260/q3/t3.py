import re
class Solution(object):
    def placeWordInCrossword(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        cand = []
        tp=""
        for i in range(m):
            for j in range(n):
                t = board[i][j]
                if t == "#":
                    if len(tp)>0:
                        cand.append(tp)
                        tp = ""
                else:
                    tp=tp+t
            cand.append(tp)
            tp = ""
        print(cand)
        for j in range(n):
            for i in range(m):
                t = board[i][j]
                if t == "#":
                    if len(tp)>0:
                        cand.append(tp)
                        tp = ""
                else:
                    tp=tp+t
            cand.append(tp)
            tp = ""
        print(cand)
        def isMatch(pattern, searc):
            m  = len(pattern)
            n = len(searc)
            if m !=n:
                return False
            #print("aaa",m,n)
            for j in range(m -n+1):
                #sprint("aaaa")
                for i in range(n):
                    t = pattern[i+j] 
                    if t == " ":
                        continue
                    elif t != searc[i]:
                        return False
                return True
        res = filter(lambda x : isMatch(x,word), cand)   
        word2 = word[::-1]
        res2 = filter(lambda x : isMatch(x,word2), cand)   
        res = list(res) + list(res2)
        print(cand)
        return len(list(res)) > 0

board = [["l","#"],[" "," "],[" "," "]]
word = "ca"

re = Solution().placeWordInCrossword(board,word)
print(re)