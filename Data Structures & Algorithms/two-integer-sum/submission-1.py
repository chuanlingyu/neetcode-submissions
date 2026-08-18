class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set_check = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in set_check:
                return [set_check[diff], i]
            else:
                set_check[nums[i]] = i