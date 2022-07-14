class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #while loop that will only break if no val is there in num
        while True:
            try:
                nums.remove(val) 
            except: break
        return len(nums)