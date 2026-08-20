class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len = len(word1)
        word2_len = len(word2)
        smaller = min(word1_len, word2_len)

        output = ""

        for i in range(smaller):
            output += word1[i]
            output += word2[i]

        if word1_len > smaller:
            output += word1[smaller:]
        elif word2_len > smaller:
            output += word2[smaller:]

        return output