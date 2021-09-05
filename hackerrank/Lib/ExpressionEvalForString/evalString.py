##Parse Expression form String and Evaluate Lisp
#https://leetcode.com/contest/weekly-contest-60/problems/parse-lisp-expression/
class Solution(object):
    def evaluate(self, expression):
        st, d, tokens = [], {}, ['']

        def getval(x):
            return d.get(x, x)

        def evaluate(tokens):
            if tokens[0] in ('add', 'mult'):
                tmp = map(int, map(getval, tokens[1:]))
                return str(tmp[0] + tmp[1] if tokens[0] == 'add' else tmp[0] * tmp[1])
            else: #let
                for i in xrange(1, len(tokens)-1, 2):
                    if tokens[i+1]:
                        d[tokens[i]] = getval(tokens[i+1])
                return getval(tokens[-1])

        for c in expression:
            if c == '(':
               # print tokens
                if tokens[0] == 'let':
                    evaluate(tokens)
                st.append((tokens, dict(d)))
                tokens =  ['']
            elif c == ' ':
                tokens.append('')
            elif c == ')':
                val = evaluate(tokens)
                tokens, d = st.pop()
                tokens[-1] += val
            else:
                tokens[-1] += c
        return int(tokens[0])




s= Solution()
expression = "(let x 1 y 2 x (add x y) (add x y))"
print s.evaluate(expression)