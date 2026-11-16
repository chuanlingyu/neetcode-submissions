class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}

        for string in strs:
            elem = {}
            for char in string:
                elem[char] = elem.get(char, 0) + 1

            key = tuple(sorted(elem.items()))

            store.setdefault(key, []).append(string)

        return list(store.values())