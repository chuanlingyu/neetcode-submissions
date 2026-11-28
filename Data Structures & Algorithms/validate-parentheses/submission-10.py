class Solution:
    def isValid(self, s: str) -> bool:
        par = {
            ')': "(",
            ']': '[',
            '}': '{'
        }

        track = []

        for char in s:
            if char in par:
                if not track or track[-1] != par[char]:
                    return False

                else:
                    track.pop()

            elif char in par.values():
                track.append(char)

        return len(track) == 0