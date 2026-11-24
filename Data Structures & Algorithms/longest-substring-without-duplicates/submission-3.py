class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        track = {}
        longest = 0

        for i in range(len(s)):
            c = s[i]
            if c in track:
                left = max(track[c] + 1, left)

            track[c] = i            
            longest = max(longest, i - left + 1)

        return longest