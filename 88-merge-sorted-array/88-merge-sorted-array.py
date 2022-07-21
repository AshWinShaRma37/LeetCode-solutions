class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #can't sure sort() function here 
        #as it returns nothing and makes changes to the original sequence
        nums1[:] = sorted(nums1[:m]+nums2[:n])