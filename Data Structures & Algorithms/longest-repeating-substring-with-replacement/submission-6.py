class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        check = {}
        left = 0
        result = 0

        for i in range(len(s)):
            num = s[i]

            check[num] = check.get(num, 0) + 1

            maxLength = max(check[num], maxLength)

            while i - left + 1 - maxLength > k:
                check[s[left]] -= 1
                left += 1

            result = max(result, i - left + 1)

        return result