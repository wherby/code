from typing import List, Tuple, Optional

def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
  
    # create lps[] that will hold the longest prefix suffix 
    # values for pattern
    lps = [0]*M
    j = 0 # index for pat[]
  
    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)
    #print(lps)
    res =[]
    i = 0 # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
  
        if j == M:
            #print("Found pattern at index " + str(i-j))
            res.append(i-j)
            j = lps[j-1]
  
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return res
  
def computeLPSArray(pat, M, lps):
    len = 0 # length of the previous longest prefix suffix
  
    lps[0] # lps[0] is always 0
    i = 1
  
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar 
            # to search step.
            if len != 0:
                len = lps[len-1]
  
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1

class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        m,n = len(grid),len(grid[0])
        st1,st2= [],[]
        idx1 ,idx2 = [],[]
        for i in range(m):
            for j in range(n):
                st1.append(grid[i][j])
                idx1.append((i,j))
        for j in range(n):
            for i in range(m):
                st2.append(grid[i][j])
                idx2.append((i,j))
        st1st = "".join(st1)
        st2st ="".join(st2)
        def getDic(st1,idx1):
            dic1 =set([])
            ret1 = KMPSearch(pattern,st1)
            m = len(pattern)
            n = len(st1)
            diff_ls = [0]*(n+1)
            for a in ret1:
                diff_ls[a] +=1
                diff_ls[a+m] -=1
            acc = 0
            for i in range(n):
                acc +=diff_ls[i]
                if acc >0:
                    dic1.add(idx1[i])
            return dic1
        ret1 = getDic(st1st,idx1)
        ret2 = getDic(st2st,idx2)
        return len(ret1&ret2)