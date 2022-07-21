class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Initialize and set maxSum to first num and currSum to 0
		#Adding first element to currSum using for loop 
        maxSum, currSum = nums[0], 0

		#Loop through nums
        for num in nums:
		
			#if currSum is less than num and the currSum is negative, 
			# the curr sem will be set to the next element 
            #as it is not fruitful to add negatives in order to get a higher sum
			
            if currSum < num and currSum < 0:
                currSum = num
            else:
			
				#Add elem to currSum
                currSum += num
				
			#Find the max between what you just computed and the overall maxSum
			# you've been keeping track of
            maxSum = max(currSum, maxSum)
        
        return maxSum