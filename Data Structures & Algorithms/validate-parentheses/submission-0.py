class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char not in matching:
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top != matching[char]:
                    return False

        return not stack