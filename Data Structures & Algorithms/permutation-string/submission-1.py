class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s1_size = len(s1)
        
        for i in range(len(s2) - s1_size + 1):
            sub = sorted(s2[i:i + s1_size])

            if sub == s1:
                return True

        return False

