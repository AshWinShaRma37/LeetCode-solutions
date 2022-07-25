class Solution:
    def tribonacci(self, n: int) -> int:
        
        # Initialize first
        # three numbers
        first = 0
        second = 1
        third = 1
        if n ==0: 
            return 0 #for T0=0 case
        elif n<3: 
            return 1 # for T1=T2=1 case
        else:
            for i in range(2,n):
                curr = first + second + third
                first = second
                second = third
                third = curr
            return curr