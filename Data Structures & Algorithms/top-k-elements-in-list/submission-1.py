class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track = {}

        for num in nums:
            track[num] = track.get(num, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)]

        for key, value in track.items():
            freq[value].append(key)

        output = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                output.append(num)

                if len(output) == k:
                    return output

        return output