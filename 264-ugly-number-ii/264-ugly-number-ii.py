class Solution:
    def nthUglyNumber(self, n: int) -> int:
        lst=[1]
        i2,i3,i5=0,0,0
        while n>len(lst):
            #creating list by multiplying 2,3 or 5 at a time
            # and then appending the min result obtained and adding the i2,i3 o i5
            #depending on the min among u2,u3 and u5
            u2 = 2*lst[i2]
            u3 = 3*lst[i3]
            u5 = 5*lst[i5]
            umin = min((u2, u3, u5))
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            lst.append(umin)
        return lst[-1]
            
            
        