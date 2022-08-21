class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        #getting the first difference
        d = arr[1] - arr[0]
        
        #checing if the array further have the same difference
        for i in range(1, len(arr) - 1):
            if arr[i+1] - arr[i] != d:
                return False
        return True
        
        