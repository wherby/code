# https://wherby.github.io/code/string/aho_corasick.html



from collections import deque


class Vertex:
    def __init__(self,p=-1,ch ="$") -> None:
        self.K = 256
        self.next = [-1]*self.K
        self.leaf = False
        self.p = p
        self.pch = ch
        self.link = -1
        self.go = [-1]*self.K
    
    def __str__(self):
        return "({0},{1},{2},{3})".format(self.pch,self.next,self.leaf,self.link)
    def __repr__(self):
        return self.__str__()
    

class AHOCorasick:
    def __init__(self) -> None:
        self.t=[Vertex()]
    
    def addString(self,str1):
        v =0
        for ch in str1:
            c = ord(ch) -ord('a')
            if self.t[v].next[c] == -1:
                node = Vertex(v,ch)
                self.t[v].next[c] = len(self.t)
                self.t.append(node)
            v = self.t[v].next[c]
        self.t[v].leaf = True
    
    def go_link(self,v):
        if self.t[v].link ==-1:
            if v ==0 or self.t[v].p ==0:
                self.t[v].link =0
            else:
                self.t[v].link = self.go(self.go_link(self.t[v].p),self.t[v].pch)
        # In go_link will add leaf check
        if self.t[self.t[v].link].leaf == True:
            print("aaa")
        return self.t[v].link

    def go(self,v,ch):
        c = ord(ch) - ord('a')
        if self.t[v].go[c] == -1:
            if self.t[v].next[c] != -1:
                self.t[v].go[c] = self.t[v].next[c]
            else:
                self.t[v].go[c] = 0 if v ==0 else self.go(self.go_link(v),ch)
        return self.t[v].go[c]
    
    def search(self,strA):
        v = 0
        for ch in strA:
            v = self.go(v,ch)
            #print(self.t[v])
            if self.t[v].leaf == True:
                print("AC")
                re =""
                s = v 
                while self.t[s].p !=-1:
                    re += self.t[s].pch
                    s =self.t[s].p
                print(re)
                
        
        
## This will miss some state for "ha" check
ac = AHOCorasick()
ac.addString("what")
ac.addString("ha")
ac.addString("hate")
ac.addString("ver")
ac.addString("er")
ac.search("whatever11")