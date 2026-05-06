class Solution:
    def isValid(self, s: str) -> bool:
        stack = [0]
        for i in range(len(s)):
            if s[i] in ['[', '{', '(']:
                stack.append(s[i])
            else:
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

        return True
                