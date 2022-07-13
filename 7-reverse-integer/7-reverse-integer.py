class Solution:
    def reverse(self, x: int) -> int:
        a = 0
        if x >= 2**31-1 or x <= -2**31: return 0
        else:
            if x>0:
                a=int(str(x)[::-1]) #converting into string to inverse it and then again converting to int to remove the 0's that might come in the beginning
            if x<0:
                a=-(int(str(-x)[::-1]))
        if a >= 2**31-1 or a <= -2**31: return 0
        else: return a
