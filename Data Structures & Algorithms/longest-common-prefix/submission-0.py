class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(list(map(len, strs)))
        first = strs[0]
        for i in range(min_len):
            char = first[i]
            for j in range(1, len(strs)):
                if strs[j][i] != char:
                    return first[:i]

        return first[:min_len]