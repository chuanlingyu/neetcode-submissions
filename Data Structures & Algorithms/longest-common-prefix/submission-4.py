class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if char != strs[j][i]:
                    return strs[0][:i]

        return strs[0]