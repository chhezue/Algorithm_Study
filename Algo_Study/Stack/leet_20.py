class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            elif c == ")":
                if not stack or stack[-1] == "[" or stack[-1] == "{":
                    return False
                stack.pop()
            elif c == "]":
                if not stack or stack[-1] == "(" or stack[-1] == "{":
                    return False
                stack.pop()
            elif c == "}":
                if not stack or stack[-1] == "[" or stack[-1] == "(":
                    return False
                stack.pop()

        if stack:
            return False

        return True

s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("([])"))
print(s.isValid("([)]"))