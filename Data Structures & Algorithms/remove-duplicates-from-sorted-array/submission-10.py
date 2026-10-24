class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        check = set()

        i = 0

        while i < len(nums):
            if nums[i] in check:
                nums.pop(i)
            else:
                check.add(nums[i])
                i += 1

        return len(nums)