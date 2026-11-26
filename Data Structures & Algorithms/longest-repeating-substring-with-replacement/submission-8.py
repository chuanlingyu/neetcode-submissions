class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        track = {}
        left = 0
        maxLength = 0
        result = 0

        for i in range(len(s)):
            val = s[i]

            track[val] = track.get(val, 0) + 1

            maxLength = max(maxLength, track[val])

            while i - left + 1 - maxLength > k:
                track[s[left]] -= 1
                left += 1

            result = max(result, i - left + 1)

        return result