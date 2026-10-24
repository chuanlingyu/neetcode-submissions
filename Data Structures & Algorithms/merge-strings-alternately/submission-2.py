class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)

        sma = len1 if len1 < len2 else len2

        output = ""

        for i in range(sma):
            output += word1[i] + word2[i]

        if len1 > len2:
            output += word1[sma:]
        elif len2 > len1:
            output += word2[sma:]

        return output