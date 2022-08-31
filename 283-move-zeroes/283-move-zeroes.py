class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #counting the total 0s
        count = nums.count(0)
        
        for i in range(count):
            nums.remove(0) #removing the first 0 appearing in list
            nums.append(0) #adding a zero at the end of list