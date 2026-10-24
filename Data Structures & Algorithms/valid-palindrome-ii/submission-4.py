class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) -1

        def extraCheck(s: str) -> bool:
            i = 0
            j = len(s) -1

            while i < j:
                if s[i].lower() != s[j].lower():
                    return False

                i += 1
                j -= 1

            return True

        while i < j:

            if s[i].lower() != s[j].lower():
                return extraCheck(s[i + 1 : j + 1]) or extraCheck(s[i:j])

            i += 1
            j -= 1

        return True