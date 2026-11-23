class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        result = 0
        store = {}
        left = 0

        for right in range(len(s)):
            right_val = s[right]

            store[right_val] = store.get(right_val, 0) + 1

            maxLength = max(maxLength, store[right_val])

            while (right - left + 1) - maxLength > k:
                store[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result