class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst = nums1+nums2 #apeending the list
        lst.sort() #orddering the list
        j = len(lst) 
        if j%2 ==1:
            return lst[int(j/2)] #if len is odd median is simply the middle guy 
        else:
            return (lst[int(j/2)]+lst[int((j/2)-1)])/2 #if len is even the median is half of the two mid elements
        
