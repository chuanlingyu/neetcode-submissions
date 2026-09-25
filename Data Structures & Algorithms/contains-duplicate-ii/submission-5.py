class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        past = set()
        for i in range(len(nums)):
            if len(past) > k:
                past.remove(nums[i - k - 1])
            if nums[i] in past:
                return True

            past.add(nums[i])

        return False