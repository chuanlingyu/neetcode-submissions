class Solution:
    def isValid(self, s: str) -> bool:
        check = []
        for char in s:
            if char == '[' or char == '{' or char == "(":
                check.append(char)
            elif char == ')':
                if len(check) == 0 or check[-1] != '(':
                    return False
                else:
                    check.pop(-1)
            elif char == ']':
                if len(check) == 0 or check[-1] != '[':
                    return False
                else:
                    check.pop(-1)
            elif char == '}':
                if len(check) == 0 or check[-1] != '{':
                    return False
                else:
                    check.pop(-1)

        return len(check) == 0