class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}

        for i in range(len(nums)):
            val = nums[i]
            diff = target - val

            if diff in track:
                return [track[diff], i]

            track[val] = i