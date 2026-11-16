class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for s in strs:
            key = ''.join(sorted(s))

            group.setdefault(key, []).append(s)

        return list(group.values())