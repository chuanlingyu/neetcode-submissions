class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        length = len(nums)
        for i in range(length):
            num = nums[i]
            for j in range(1, k + 1):
                if i + j >= length:
                    break
                if num == nums[i + j]:
                    return True

        return False