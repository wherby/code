#https://leetcode.cn/contest/hhrc2022/ranking/1/
class Solution(object):
    def longestESR(self, sales):
        """
        :type sales: List[int]
        :rtype: int
        """
        n = len(sales)
        left =0
        acc =0
        mx = 0
        for i,a in enumerate(sales):
            #print(acc,i,left,"a"*2)
            if a > 8:
                acc +=1
                while (acc >1 and left >0 and sales[left-1] <=8) or (acc >=0 and left >0 and sales[left-1] >8) :
                    left-=1
                    if sales[left]>8:
                        acc +=1
                    else:
                        acc -=1
            else:
                acc -=1
                while acc <0 and left <= i:
                    if sales[left]>8:
                        acc -=1
                    else:
                        acc +=1
                    left +=1
            print(i,left,acc)
            if acc >=1:
                mx = max(mx,i-left+1)
        return mx
                
re =Solution().longestESR([10,8,8,12,6,6,7,11,11,9,11])
print(re)