class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track = {}

        for s in strs:
            val = "".join(sorted(s))
            track.setdefault(val, []).append(s)

        return list(track.values())

        # output = [[] for _ in range(len(strs) + 1)]

        # for key, value in track.items():
        #     output[val].append(key)