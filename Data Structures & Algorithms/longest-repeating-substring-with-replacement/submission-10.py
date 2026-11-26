class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        track = {}
        l = 0
        res = 0
        maxLength = 0

        for r in range(len(s)):
            val = s[r]
            track[val] = track.get(val, 0) + 1

            maxLength = max(maxLength, track[val])

            while r - l + 1 - maxLength > k:
                track[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res