class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = {
            ']' : '[',
            '}' : '{',
            ")" : "("
        }

        for char in s:
            if char in check:
                if not stack:
                    return False
                elif stack[-1] == check[char]:
                    stack.pop()
                else:
                    return False
            elif char in check.values():
                stack.append(char)
                
        if not stack:
            return True
        
        return False