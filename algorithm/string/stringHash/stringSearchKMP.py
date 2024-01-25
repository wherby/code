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
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        aidx =KMPSearch(a,s)
        bidx =KMPSearch(b,s)
        bidx = [-10**10] +bidx + [10**10]
        m = len(bidx)
        l = 0 
        ret =[]
        
        for ai in aidx:
            while l< m and bidx[l+1]<=ai:
                l +=1
            if abs(ai - bidx[l]) <= k or abs(bidx[l+1] -ai) <=k:
                ret.append(ai)
        return ret

re =Solution().beautifulIndices(s = "isawsquirrelnearmysquirrelhouseohmy", a = "my", b = "squirrel", k = 15)
print(re)