class Solution:
    def isValid(self, s: str) -> bool:
        par = {
            '}': '{',
            ')': '(',
            ']': '['
        }

        track = []

        for c in s:
            if c in par:
                if len(track) == 0:
                    return False
                elif par[c] == track[-1]:
                    track.pop()
                else:
                    return False
            elif c in par.values():
                track.append(c)

        return True if len(track) == 0 else False