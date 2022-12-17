# https://leetcode.cn/problems/form-array-by-concatenating-subarrays-of-another-array/submissions/
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
    i = 0 # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
  
        if j == M:
            return i-M 
  
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return -1
  
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
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        for g in groups:
            k = KMPSearch(g,nums)
            #print(k,g, nums)
            if k == -1:
                return False
            nums= nums[k+ len(g):]
        return True
                
        
        
gs=[[6551094,9427527,2052462,3481286,-7620442],[8495362,-1820796],[-1005271,-6911519],[-9667242,9997184,-9316362],[-9278108,-7479063,-7573091,-1775876,-2612810,-241649]]
nums=[6551094,6551094,9427527,2052462,3481286,-7620442,-7620442,8495362,-1820796,-1005271,-6911519,-9667242,9997184,-9316362,9997184,-9278108,-7479063,-7573091,-1775876,-2612810,-241649]
re = Solution().canChoose(groups =gs, nums=nums)
print(re)