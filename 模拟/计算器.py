class Solution:
    def calculate(self, s: str) -> int:

        def transfer(s):
            ast = []
            res = []
            tmp = ""
            for i in range(len(s)):
                if s[i] in ("+", "-"):
                    res.append(tmp)
                    tmp = ""
                    while ast:
                        res.append(ast.pop())
                    ast.append(s[i])
                elif s[i] in ("*", "/"):
                    res.append(tmp)
                    tmp = ""
                    while ast and ast[-1] in ("*", "/"):
                        res.append(ast.pop())
                    ast.append(s[i])
                else:
                    tmp += s[i]
            res.append(tmp)
            while ast:
                res.append(ast.pop())
            return res
        def cal(l):
            ast = []
            for i in range(len(l)):
                if l[i] not in ("+", "-", "*", "/"):
                    ast.append(l[i])
                else:
                    b = int(ast.pop())
                    a = int(ast.pop())
                    if l[i] == "+":
                        ast.append(a + b)
                    elif l[i] == "-":
                        ast.append(a - b)
                    elif l[i] == "*":
                        ast.append(a * b)
                    else:
                        ast.append(a // b)
            return ast[0]

        s = ("".join(s.split()))
        return int(cal(transfer(s)))
