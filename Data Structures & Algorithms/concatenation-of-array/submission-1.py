class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        output = list(range(len(nums) * 2))
        for i in range(len(nums)):
            output[i] = nums[i]
            output[i + len(nums)] = nums[i]

        return output