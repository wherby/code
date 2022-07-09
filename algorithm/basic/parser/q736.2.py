from collections import defaultdict,deque
class Solution:
    def evaluate(self, expression: str) -> int:
        isvar = lambda x: isinstance(x, str) and x[0].isalpha()
        def cal(cmd, d={}):
            if isinstance(cmd, str):
                return d[cmd] if isvar(cmd) else int(cmd)
            result = 0
            while cmd:
                v = cmd.popleft()
                if v == 'add':
                    result = cal(cmd.popleft(), d.copy()) + cal(cmd.popleft(), d.copy())
                elif v == 'mult':
                    result = cal(cmd.popleft(), d.copy()) * cal(cmd.popleft(), d.copy())
                elif v == 'let':
                    while len(cmd) > 1 and isvar(cmd[0]):
                        key, value = cmd.popleft(), cmd.popleft()
                        d[key] = cal(value, d.copy())
                else:
                    result = cal(v, d.copy())
            return result
        
        parents = [deque()]
        for word in expression[1:-1].split():
            #print(word)
            if word.startswith('('):
                parents.append(deque())
                word = word[1:]
            parents[-1].append(word.rstrip(')'))
            for _ in range(word.count(')')):
                obj = parents.pop()
                parents[-1].append(obj)
        #print(parents)
        return cal(parents[0])
    
re = Solution().evaluate(expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))")
print(re)