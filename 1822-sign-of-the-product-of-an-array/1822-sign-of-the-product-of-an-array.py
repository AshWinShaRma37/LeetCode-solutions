class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        #checking if 0 present
        #then the answer is directly 0
        if (0 in nums):
            return 0
        #multiplying by -1  every time a negative number is present
        for n in nums:
            if n<0: ans =ans*-1
        return ans