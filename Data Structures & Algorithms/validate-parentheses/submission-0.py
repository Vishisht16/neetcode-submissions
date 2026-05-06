class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        halfway = int(len(s) / 2)
        stack = []

        for i in range(halfway):
            stack.append(s[i])
        
        for i in range(halfway, len(s)):
            if stack[-1] + s[i] == '[]' or stack[-1] + s[i] == '{}' or stack[-1] + s[i] == '()':
                stack.pop()
            
            else:
                return False
        
        return True