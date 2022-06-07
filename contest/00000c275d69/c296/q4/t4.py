from collections import deque
class TextEditor(object):

    def __init__(self):
        self.left =[]
        self.right =deque([])
        


    def addText(self, text):
        """
        :type text: str
        :rtype: None
        """
        for a in text:
            self.left.append(a)


    def deleteText(self, k):
        """
        :type k: int
        :rtype: int
        """
        cnt =0
        while k >0 and len(self.left)>0:
            k -=1
            cnt +=1
            self.left.pop()
        return cnt


    def cursorLeft(self, k):
        """
        :type k: int
        :rtype: str
        """
        while k >0 and len(self.left)>0:
            k -=1
            a = self.left.pop()
            self.right.appendleft(a)
        tls = self.left[-10:]
        return "".join(tls)

    def cursorRight(self, k):
        """
        :type k: int
        :rtype: str
        """
        while k >0 and len(self.right)>0:
            k -=1
            a = self.right.popleft()
            self.left.append(a)
        tls = self.left[-10:]
        return "".join(tls)
