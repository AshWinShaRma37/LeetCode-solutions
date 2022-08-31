class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []   #to create a list for checking the greatest element
        mapping = {} #dictionary to map next greatest element
        for n in nums2:
            while stack and n > stack[-1]:
                #removing the last element of list as we found a greater number
                mapping[stack.pop()] = n
            stack.append(n)
        #returning the map along with mapping elements that are not mapped to -1
        return [mapping.get(n, -1) for n in nums1]
                