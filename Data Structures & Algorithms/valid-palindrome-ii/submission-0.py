class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return self.noChance(s[i:j]) or self.noChance(s[i + 1:j + 1])                 
            i += 1
            j -= 1   

        return True

    def noChance(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
                  
            i += 1
            j -= 1

        return True