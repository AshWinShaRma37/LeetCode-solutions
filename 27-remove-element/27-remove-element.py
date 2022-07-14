class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #counting number of val in nums and then removing it that many times
        for i in range(nums.count(val)):
            nums.remove(val)
        return len(nums)