dic={}
class Solution:
    def deleteDuplicateFolder(self, paths):
        dic.clear()
        removed= []
        for s in paths:
            key = s[-1]
            if key not in dic:
                dic[key] = s
                #print(dic)
            else:
                removed.append(key)
                if len(s)>1:
                    removed.append(s[-2])
                if len(dic[key])>1:
                    removed.append(dic[key][-2])
                print(s)
                dic[key] = []
        print(removed)
        for key in  removed:
            dic[key] =[]
        re= []
        for k,v in dic.items():
            re.append(v)
        print(re)
        re = list(filter(lambda x:len(x)>0,re))
        print(re)
        return re
        
        

a =Solution().deleteDuplicateFolder([["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]])