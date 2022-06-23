## This combine aho-corasick and aho-corasick2
## 

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
        self.output =[]
    
    def __str__(self):
        return "({0},{1},{2},{3})".format(self.pch,self.output,self.leaf,self.link)
    def __repr__(self):
        return self.__str__()
    
class AHOCorasick:
    def __init__(self,keywords =[]) -> None:
        self.t= [Vertex()]
        for key in keywords:
            self.addString(key)
        self.set_fail_transitions()
        
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
        self.t[v].output.append(str1)
    
    def go_link(self,v):
        if self.t[v].link ==-1:
            if v ==0 or self.t[v].p ==0:
                self.t[v].link =0
            else:
                self.t[v].link = self.go(self.go_link(self.t[v].p),self.t[v].pch)
        return self.t[v].link

    def go(self,v,ch):
        c = ord(ch) - ord('a')
        if self.t[v].go[c] == -1:
            if self.t[v].next[c] != -1:
                self.t[v].go[c] = self.t[v].next[c]
            else:
                self.t[v].go[c] = 0 if v ==0 else self.go(self.go_link(v),ch)
        return self.t[v].go[c]
    
    def set_fail_transitions(self):
        q = deque()
        for s in self.t[0].next:
            if s ==-1: continue
            q.append(s)
        while q :
            r = q.popleft()
            for s in self.t[r].next:
                if s ==-1:continue
                q.append(s)
            self.go_link(r)
            #print(self.t[r].link,s)
            self.t[r].output.extend(self.t[self.t[r].link].output)
    
    def search_in(self,string):
        """
        >>> A = AHOCorasick(["what", "hat", "ver", "er"])
        >>> A.search_in("whatever, err ... , wherever")
        {'what': [0], 'hat': [1], 'ver': [5, 25], 'er': [6, 10, 22, 26]}
        """
        result =dict()
        v =0
        for i in range(len(string)):
            #print(self.t[v])
            v=self.go(v,string[i])
            for key in self.t[v].output:
                if not (key in result):
                    result[key] =[]
                result[key].append(i-len(key)+1)
        return result



if __name__ == "__main__":
    import doctest
    doctest.testmod()
else:
    ac = AHOCorasick()
    ac.addString("what")
    ac.addString("ha")
    ac.addString("hate")
    ac.addString("er")
    ac.addString("ver")
    ac.set_fail_transitions()
    re =ac.search_in("whatever, err ... , wherever")
    print(re)
#print(ac.t)            
                
                    
                
        
        