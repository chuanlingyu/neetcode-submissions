class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}

        for s in strs:
            val = "".join(sorted(s))

            output.setdefault(val, []).append(s)
            
        return list(output.values())