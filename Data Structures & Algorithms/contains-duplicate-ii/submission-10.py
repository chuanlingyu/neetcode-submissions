class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        check = set()

        for i in range(len(nums)):
            if len(check) > k:
                check.remove(nums[i - k - 1])

            if nums[i] in check:
                return True

            check.add(nums[i])

        return False