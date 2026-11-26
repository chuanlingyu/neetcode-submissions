class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track = {}

        for s in strs:
            word = ''.join(sorted(s))

            track.setdefault(word, []).append(s)

        return list(track.values())