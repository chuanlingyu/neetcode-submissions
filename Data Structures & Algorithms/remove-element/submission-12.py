class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        begin = 0
        end = len(nums)

        while begin < end:
            if nums[begin] == val:
                nums[begin] = nums[end - 1]
                end -= 1
            else:
                begin += 1

        return begin