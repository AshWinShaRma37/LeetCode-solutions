class Solution:
    def climbStairs(self, n: int) -> int:
        i=0
        a = b = 1
        #Using kind of induction
        # a is the number of ways to reach the current step
        # b is the number of ways to reach the next step after the current step
        # so a+b is the number of steps for the next step altogether 
        while i<n:
            a, b = b, a + b
            i=i+1
        return a