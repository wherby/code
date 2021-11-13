from collections import defaultdict
class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        ls2 = [2** i for i in range(22)]
        #print(ls2)
        cnt =0
        dic  = defaultdict(int)
        for d in deliciousness:
            dic[d] +=1
        #print(dic)
        for k,v in dic.items():
            for l2  in ls2:
                t = l2 -k
                if t in dic:
                    v2 = dic[t]
                    if t ==k:
                        cnt += v * (v-1)/2
                    else:
                        cnt += v * v2 /2
        #print(cnt)
        return int(cnt)% (10**9 +7)

re =Solution().countPairs(deliciousness =[2160,1936,3,29,27,5,2503,1593,2,0,16,0,3860,28908,6,2,15,49,6246,1946,23,105,7996,196,0,2,55,457,5,3,924,7268,16,48,4,0,12,116,2628,1468])
print(re)