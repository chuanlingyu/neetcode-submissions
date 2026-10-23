class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # curr = 0
        # end = len(nums) - 1
        # while curr < end:
        #     if nums[curr] == val:
        #         tmp = nums[curr]
        #         nums[curr] = nums[end]
        #         nums[end] = tmp
        #         end -= 1
        #     else:
        #         curr += 1

        # return curr + 1

        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)

            else:
                i += 1

        return i