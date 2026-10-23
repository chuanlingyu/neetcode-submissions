class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = min(list(map(len, strs)))
        for i in range(0, smallest):
            first = strs[0][i]
            for j in range(1, len(strs)):
                if (strs[j][i]) != first:
                    return strs[0][:i]

        return strs[0][:smallest]