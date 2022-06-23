# https://stackoverflow.com/questions/66198575/typeerror-not-supported-between-instances-of-node-and-node

class Node:
    def __init__(self,l,r,w):
        self.l =l
        self.r =r
        self.w =w 
    
    def __ge__(self,other):
        return (self.l,self.r,self.w) >(other.l,other.r,other.w)
    
    def __lt__(self,other):
        return (self.l,self.r,self.w) <(other.l,other.r,other.w)
    def __str__(self):
        return "({0},{1},{2})".format(self.l,self.r,self.w)
    def __repr__(self):
        return "({0},{1},{2})".format(self.l,self.r,self.w)