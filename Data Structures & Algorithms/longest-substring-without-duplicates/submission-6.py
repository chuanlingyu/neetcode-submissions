class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = {}
        l = 0
        res = 0

        for r in range(len(s)):
            val = s[r]

            if val in track:
                l = max(l, track[val] + 1)

            track[val] = r
            res = max(res, r - l + 1)

        return res