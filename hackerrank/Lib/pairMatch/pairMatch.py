##pair match for alternative chars
## pair math "(" and ")"  "*" can be "(" or ")" or None

class PairMatch(object):
    def checkValidString(self, s):
        lo = hi = 0
        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            if hi < 0: break
            lo = max(lo, 0)

        return lo == 0

if __name__=="__main__":
	pm = PairMatch()
	print pm.checkValidString("(******((((())")
	print pm.checkValidString("(******(())")
	print pm.checkValidString("())***())")