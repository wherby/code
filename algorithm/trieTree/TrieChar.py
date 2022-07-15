class node:
    def __init__(self) -> None:
        self.child ={}
        self.ls=[]
        self.is_end = False
        
class TrieTree():
    def __init__(self) -> None:
        self.root =node()
    
    def insert(self,word,idx):
        cur = self.root
        for a in word:
            if a not in cur.child:
                cur.child[a] =node()
            cur = cur.child[a]
            cur.ls.append(idx)
        cur.is_end  =True
    
    def get(self,pre):
        cur = self.root
        for a in pre:
            if a not in cur.child:
                return []
            else:
                cur = cur.child[a]