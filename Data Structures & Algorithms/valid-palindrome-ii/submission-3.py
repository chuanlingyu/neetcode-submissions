class Solution:
    def testPali(self, s: str) -> bool:
        length = len(s)
        for i in range(length // 2):
            if s[i] != s[length - 1 - i]:
                return False

        return True

    def validPalindrome(self, s: str) -> bool:
        length = len(s)
        for i in range(length // 2):
            if s[i] != s[length - 1 - i]:
                return self.testPali(s[i:length - i - 1]) or self.testPali(s[i + 1:length - i])

        return True