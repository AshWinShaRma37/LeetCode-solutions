class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # sorting the list to get the max at end 
        # making it easier to check the condition for a triangle
        # that if a,b,c are sides of a triangle
        # a+b>c
        nums.sort()
        for i in range(len(nums) - 3, -1, -1):
            if nums[i] + nums[i+1] > nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0