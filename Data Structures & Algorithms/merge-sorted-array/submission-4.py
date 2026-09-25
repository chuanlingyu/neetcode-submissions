class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        track = m + n - 1
        m -= 1
        n -= 1
        while (track >= 0 and n >= 0 and m >= 0):
            if nums1[m] > nums2[n]:
                nums1[track] = nums1[m]
                m -= 1
            else:
                nums1[track] = nums2[n]
                n -= 1
            
            track -= 1

        while (n >= 0):
            nums1[n] = nums2[n]
            n -= 1