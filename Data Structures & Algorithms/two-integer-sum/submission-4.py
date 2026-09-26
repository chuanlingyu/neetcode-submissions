class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num;
            if diff in check:
                return [check[diff], i]
            else:
                check[num] = i