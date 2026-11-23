class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = set()
        left = 0
        maximum = 0

        for right in range(len(s)):
            while s[right] in track:
                track.remove(s[left])
                left += 1

            track.add(s[right])
            maximum = max(maximum, right - left + 1)

        return maximum