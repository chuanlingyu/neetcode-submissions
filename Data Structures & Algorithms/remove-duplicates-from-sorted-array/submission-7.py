class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        exist = set()
        k = 0
        for num in nums:
            if num not in exist:
                exist.add(num)
                nums[k] = num
                k += 1 

        return k