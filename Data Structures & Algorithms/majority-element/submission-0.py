class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        check = {}
        length = len(nums) // 2

        for num in nums:
            check[num] = check.get(num, 0) + 1
            if check[num] > length:
                return num