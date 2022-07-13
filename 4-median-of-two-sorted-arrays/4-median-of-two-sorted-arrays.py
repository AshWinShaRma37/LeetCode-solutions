class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst = nums1+nums2
        lst.sort()
        j = len(lst)
        if j%2 ==1:
            return lst[int(j/2)]
        else:
            return (lst[int(j/2)]+lst[int((j/2)-1)])/2
        