# algorithm/codeforce/dp/状态转移套状态转移.py
# https://codeforces.com/gym/103306/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0715/solution/cf103306a.md

def getSubWithHigestBit(msk):
    bit = 1 << msk.bit_length() - 1 
    cur = msk 
    ret = [] 
    
    while cur >= bit:
        ret.append(cur )
        cur = (cur-1)&msk 
    return ret 

ls = getSubWithHigestBit(29)
print(ls)