import collections
class Solution:
    def distinctNames(self, ideas) -> int:
        dictt = collections.defaultdict(set)
        for t in ideas :
            dictt[t[1:]].add(t[0])
        
        cs = 'abcdefghijklmnopqrstuvwxyz'
        cts = {a:{b:0 for b in cs} for a in cs}
        #cts[a][b] 表示，之前以a为开头，且可以和b开头的互换的，有多少个。
        
        
        to_ret = 0
        for ktail in dictt :
            vhead = dictt[ktail]
            print(vhead,ktail)
            for ht in vhead :
                for a in cts :
                    if a in vhead :
                        continue
                    to_ret += cts[a][ht]
            
            for ht in vhead :
                for a in cs :
                    if a in vhead :
                        continue
                    cts[ht][a] += 1
        return to_ret * 2
                
re =Solution().distinctNames(ideas =["aaa","baa","caa","bbb","cbb","dbb"])
print(re)