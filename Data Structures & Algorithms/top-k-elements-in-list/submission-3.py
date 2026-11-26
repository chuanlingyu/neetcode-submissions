class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track = {}

        for num in nums:
            track[num] = track.get(num, 0) + 1
        
        output = [[] for _ in range(len(nums) + 1)]

        for key, value in track.items():
            output[value].append(key)

        result = []

        for i in range(len(output) - 1, 0, -1):
            for num in output[i]:
                result.append(num)

                if len(result) == k:
                    return result

        return result