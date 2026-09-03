class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        length = min(len(word1), len(word2))

        for i in range(length):
            output += word1[i]
            output += word2[i]

        if len(word1) > length:
            output += word1[length:]
        elif len(word2) > length:
            output += word2[length:]

        return output