class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #set(nums) contains no duplicates
        #hence simply checking if set(nums) and nums have same length
        return len(set(nums)) != len(nums)
