class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.casefold()
        i = 0
        j = len(s) - 1
        while i <= j:
            while i < j and not (s[i].isnumeric() or s[i].isalpha()):
                i += 1

            while j > i and not (s[j].isnumeric() or s[j].isalpha()):
                j -= 1

            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1

        return True