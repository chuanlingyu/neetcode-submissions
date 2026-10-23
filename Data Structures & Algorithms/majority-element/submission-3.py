class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        check = {}
        half = len(nums) / 2

        for num in nums:
            check[num] = check.get(num, 0) + 1
            if check[num] > half:
                return num