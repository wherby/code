# 用treTree 里编码string,用cur 来充当前缀hash 值

class node:
    def __init__(self,cur =0,cnt = 0) -> None:
        self.child ={}
        self.cur = cur 
        self.cnt = cnt

class Trie:
    def __init__(self) -> None:
        self.root = node()
        self.idx = 0
    
    def insert(self,w):
        r = self.root
        for i in w:
            if i not in r.child:
                r.child[i] = node(self.idx)
                self.idx +=1
            r = r.child[i]
            r.cnt +=1
    
    
    def get(self,x):
        r =self.root
        if len(r.child) == 0:
            return -1
        ret = []
        for i in x:
            r =r.child[i]
            ret.append(r.cur)
        return ret
    
    def __repr__(self):
        def recur(node, indent):
            return "".join(indent + str(key) +" "+str(ch.cur)+" " +str(ch.cnt)  + recur(ch, indent + "  ")  for key, ch in node.child.items())
        return recur(self.root, "\n")


tre = Trie()
tre.insert("hello")
tre.insert("her")
tre.insert("world")
print(tre.get("worl"))
print(tre.get("hello"))
print(tre.get("her"))
print(tre)