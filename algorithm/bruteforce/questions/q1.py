# https://leetcode.cn/contest/zj-future2022/problems/NBCXIp/
# https://leetcode.cn/contest/zj-future2022/ranking/1/
#某连锁店开设了若干门店，门店间允许进行商品借调以应对暂时性的短缺。本月商品借调的情况记于数组 distributions，其中 distributions[i] = [from,to,num]，表示从 from 门店调配了 num 件商品给 to 门店。
#若要使得每一个门店最终借出和借入的商品数量相同，请问至少还需要进行多少次商品调配。
#注意：一次商品调配以三元组 [from, to, num] 表示，并有 from ≠ to 且 num > 0。
#1 <= distributions.length <= 8
#distributions[i].length == 3
#0 <= fromi, toi < 12
#fromi != toi
#1 <= numi <= 100


class Solution(object):
    def minTransfers(self, distributions):
        """
        :type distributions: List[List[int]]
        :rtype: int
        """
        nums = [0]*12
        for f,t,n in distributions:
            nums[f] -=n
            nums[t] +=n
        mn = 16
       
        def backTrack(index,cnt):
            nonlocal mn
            while index<12 and nums[index] ==0 : # 如果没有这里，index 不会变成12
                index +=1
            if cnt > mn:
                return
            if index == 12:
                mn = min(mn,cnt) 
                return

            for i in range(index+1,12):
                if nums[index] * nums[i] >=0:  # 剪枝
                    continue
                nums[i] += nums[index]
                backTrack(index +1, cnt + (nums[index] !=0))
                nums[i] -= nums[index]
        backTrack(0,0)
        return mn
    
re =Solution().minTransfers([[1,8,1],[1,0,21],[2,8,10],[3,9,20],[4,10,61],[5,11,61],[6,1,59],[7,0,60]])
print(re)