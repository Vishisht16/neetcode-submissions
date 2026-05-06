class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []

        for i in range(len(s)):
            if s[i] in ['[', '{', '(']:
                stack.append(s[i])

            else:
                if len(stack) == 0:
                    return False

                last = stack.pop()

                if last == '[':
                    if s[i] == ']':
                        continue
                    else:
                        return False

                elif last == '(':
                    if s[i] == ')':
                        continue
                    else:
                        return False

                elif last == '{':
                    if s[i] == '}':
                        continue
                    else:
                        return False
        
        if len(stack) == 0:
            return True
        
        else:
            return False
                