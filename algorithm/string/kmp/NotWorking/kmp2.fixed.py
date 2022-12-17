#https://www.codespeedy.com/kmp-string-matching-algorithm-in-python/ 
# Fixed
from typing import List, Tuple, Optional
def KMP_String(pattern, text):
    a = len(text)
    b = len(pattern)
    prefix_arr = get_prefix_arr(pattern, b)
    initial_point = []
    m = 0
    n = 0
  
    while m != a:
        if text[m] == pattern[n]:
            m += 1
            n += 1

        elif n !=0:
            n = prefix_arr[n-1]
        else:
            m +=1
        if n == b:
            return m-n 
        # elif  n == 0:
        #     m += 1
   
    return -1
def get_prefix_arr(pattern, b):
    prefix_arr = [0] * b
    n = 0
    m = 1
    while m != b:
        if pattern[m] == pattern[n]:
            n += 1
            prefix_arr[m] = n
            m += 1
        elif n != 0:
                n = prefix_arr[n-1]
        else:
            prefix_arr[m] = 0
            m += 1
    #print(prefix_arr)
    return prefix_arr



class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        for g in groups:
            k = KMP_String(g,nums)
            #print(k,g, nums)
            if k == -1:
                return False
            nums= nums[k+ len(g):]
        return True
                
        
        
gs=[[6551094,9427527,2052462,3481286,-7620442],[8495362,-1820796],[-1005271,-6911519],[-9667242,9997184,-9316362],[-9278108,-7479063,-7573091,-1775876,-2612810,-241649]]
nums=[6551094,6551094,9427527,2052462,3481286,-7620442,-7620442,8495362,-1820796,-1005271,-6911519,-9667242,9997184,-9316362,9997184,-9278108,-7479063,-7573091,-1775876,-2612810,-241649]
re = Solution().canChoose(groups =gs, nums=nums)
print(re)