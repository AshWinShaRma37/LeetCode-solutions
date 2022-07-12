class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {} #create dictionary wto store num in nums with their index
        for i, num in enumerate(nums):
            #find target - num in dic along with creating dictionary with num in nums with their index
            if target - num in dic:
                return dic[target-num], i
            dic[num] = i
