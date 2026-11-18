class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}

        for s in strs:
            key = "".join(sorted(s))

            output.setdefault(key, []).append(s)

        return list(output.values())