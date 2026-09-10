class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        contain = set()
        L = 0
        for R in range(len(nums)):
            if len(contain) > k:
                contain.remove(nums[L])
                L += 1

            if nums[R] in contain:
                return True

            contain.add(nums[R])

        return False