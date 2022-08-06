# https://leetcode.com/contest/weekly-contest-262/problems/partition-array-into-two-arrays-to-minimize-sum-difference/
def getNear(ls1,ls2,val):
    mx = 10**10
    n =len(ls2)
    ridx = n-1
    for a in ls1:
        mx = min(mx,abs(a + ls2[ridx]-val))
        while ridx >0  and a + ls2[ridx]>val:
            ridx -=1
            mx =min(mx,abs(a + ls2[ridx]-val))
        mx =min(mx,abs(a + ls2[ridx]-val))
    return mx
                








ls1 = [1,4,6,8,9]
ls2 =[10,13,14,16]
print(getNear(ls1,ls2,13))