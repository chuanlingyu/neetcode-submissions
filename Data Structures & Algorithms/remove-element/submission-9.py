class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr = 0
        end = len(nums)
        while curr < end:
            if nums[curr] == val:
                end -= 1
                nums[curr] = nums[end]
            else:
                curr += 1

        return curr

        # i = 0
        # while i < len(nums):
        #     if nums[i] == val:
        #         nums.pop(i)

        #     else:
        #         i += 1

        # return i