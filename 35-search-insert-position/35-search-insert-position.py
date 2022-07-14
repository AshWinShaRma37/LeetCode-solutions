class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #setting up low and high index
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            #if target is less than mid number of list then changing high index to mid-1
            if target < nums[mid]:
                high = mid - 1
            #if target is greater than mid number of list then changing low index to mid+1
            elif target > nums[mid]:
                low = mid + 1
            else:
                return mid
        return low