class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        begin = 0
        end = len(nums)

        while begin < end:
            if nums[begin] == val:
                end -= 1
                nums[begin] = nums[end]
            else:
                begin += 1

        return begin