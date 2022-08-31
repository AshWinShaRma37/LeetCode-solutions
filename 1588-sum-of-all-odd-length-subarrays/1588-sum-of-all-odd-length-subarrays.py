class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res =0
        
        for i in range(len(arr)):
            #creating arrays of odd lengths 
            #and simply adding them and not storing them in a variable
            for j in range(i,len(arr),2):
                res = res + sum(arr[i:j+1])
        return res