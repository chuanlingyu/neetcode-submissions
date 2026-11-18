class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        output = [[] for _ in range(len(nums) + 1)]

        for key, value in count.items():
            output[value].append(key)

        result = []

        for i in range(len(output) - 1, 0, -1):
            for num in output[i]:
                result.append(num)

                if len(result) == k:
                    return result

        return result