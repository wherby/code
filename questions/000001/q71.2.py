
class Solution(object):
    def simplifyPath(self, path):
        ns = path.split("/")
        ret =[]
        for a in ns:
            if a =="" or a ==".":
                continue
            if a =="..":
                if len(ret)>0:
                    ret.pop()
            else:
                ret.append(a)
        return "/" + "/".join(ret)