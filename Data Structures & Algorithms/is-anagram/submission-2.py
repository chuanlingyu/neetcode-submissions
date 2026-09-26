class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        length = len(s)
        if length != len(t): 
            return False

        check1 = {}
        check2 = {}

        for i in range(len(s)):
            check1[s[i]] = check1.get(s[i], 0) + 1
            check2[t[i]] = check2.get(t[i], 0) + 1

        return check1 == check2