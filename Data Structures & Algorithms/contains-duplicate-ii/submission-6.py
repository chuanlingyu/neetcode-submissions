class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        check = deque()

        for i in range(len(nums)):
            if len(check) > k:
                check.popleft()

            if nums[i] in check:
                return True

            check.append(nums[i])

        return False