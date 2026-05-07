class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = int(tokens[0])

        for i in range(1, len(tokens), 2):

            if tokens[i + 1] == '+':
                res += int(tokens[i])
            elif tokens[i + 1] == '-':
                res -= int(tokens[i])
            elif tokens[i + 1] == '*':
                res *= int(tokens[i])
            else:
                res = int(res / int(tokens[i]))
        
        return res