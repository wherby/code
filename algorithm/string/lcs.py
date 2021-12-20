# longest common subsequence(lcs)
import functools
@functools.lru_cache(None)
def lcs(str1,str2):
    if not str1 or not str2:
        return ""
    if str1[0] == str2[0]:
        return str1[0] + lcs(str1[1:],str2[1:])
    else:
        return  max(lcs(str1,str2[1:]),lcs(str1[1:],str2),key=len)

print(lcs("abds","bdsad"))